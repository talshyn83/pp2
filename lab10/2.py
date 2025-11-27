import pygame 
import sys 
import random 
import psycopg2 

pygame.init() 
 
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0) 
RED = (255, 0, 0) 
WALL_COLOR = (169, 169, 169) 

snake_pos = [[100, 50], [90, 50], [80, 50]] 
snake_speed = [10, 0] 
food = {'pos': [0, 0], 'weight': 1, 'spawn_time': 0} 
food_spawn = True 
score = 0 
level = 1 
speed_increase = 0.1 
food_counter = 0   
walls = []
 
fps = pygame.time.Clock() 
paused = False 

def ensure_table_exists():
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="bnqvvs_07", port=5432)
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE
        );
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER,
            level INTEGER
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()

def insert_user(username):
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="bnqvvs_07", port=5432)
    cur = conn.cursor()
    
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    
    if not user:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    else:
        user_id = user[0]
    
    cur.close()
    conn.close()
    
    return user_id

def insert_score(user_id, score, level):
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="bnqvvs_07", port=5432)
    cur = conn.cursor() 
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level)) 
    conn.commit() 
    cur.close() 
    conn.close()

def get_user_level(username):
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="bnqvvs_07", port=5432)
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY score DESC LIMIT 1", (user[0],))
        score_data = cur.fetchone()
        cur.close()
        conn.close()
        return user[0], score_data
    else:
        cur.close()
        conn.close()
        return None, None

def set_walls_for_level(level):
    walls.clear()
    if level == 1:
        walls.extend([[x, 0] for x in range(0, SCREEN_WIDTH, 20)])
        walls.extend([[x, SCREEN_HEIGHT - 10] for x in range(0, SCREEN_WIDTH, 20)])
    elif level == 2:
        walls.extend([[x, SCREEN_HEIGHT // 2] for x in range(0, SCREEN_WIDTH, 20)])

def check_wall_collision(pos):
    return pos in walls

def get_random_food(): 
    global food_counter 
    while True: 
        pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10] 
        if pos not in snake_pos and pos not in walls: 
            weight = 2 if food_counter >= 2 else 1 
            food_counter = 0 if weight == 2 else food_counter + 1 
            return {'pos': pos, 'weight': weight, 'spawn_time': pygame.time.get_ticks()} 

def check_collision(pos): 
    if pos[0] < 0 or pos[0] > SCREEN_WIDTH - 10 or pos[1] < 0 or pos[1] > SCREEN_HEIGHT - 10: 
        return True 
    if pos in snake_pos[1:]: 
        return True 
    if check_wall_collision(pos):
        return True
    return False 

ensure_table_exists()
player_name = input("Enter your name: ") 
player_name = player_name.encode('utf-8', 'ignore').decode('utf-8') 
player_id, user_data = get_user_level(player_name)

if user_data:
    score, level = user_data
    print(f"Your previous score: {score}, level: {level}")
else:
    level = 1
    score = 0
    player_id = insert_user(player_name)

set_walls_for_level(level)

try: 
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                insert_score(player_id, score, level)
                pygame.quit() 
                sys.exit() 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP and snake_speed[1] == 0: 
                    snake_speed = [0, -10] 
                elif event.key == pygame.K_DOWN and snake_speed[1] == 0: 
                    snake_speed = [0, 10] 
                elif event.key == pygame.K_LEFT and snake_speed[0] == 0: 
                    snake_speed = [-10, 0] 
                elif event.key == pygame.K_RIGHT and snake_speed[0] == 0: 
                    snake_speed = [10, 0] 
                elif event.key == pygame.K_p: 
                    paused = not paused
                elif event.key == pygame.K_s: 
                    insert_score(player_id, score, level)
                    print("Game saved!")
 
        if not paused: 
            snake_pos.insert(0, list(map(lambda x, y: x + y, snake_pos[0], snake_speed))) 
 
            if check_collision(snake_pos[0]): 
                insert_score(player_id, score, level) 
                pygame.quit() 
                sys.exit() 
 
            if snake_pos[0] == food['pos']: 
                score += food['weight'] 
                if score % 3 == 0: 
                    level += 1
                    set_walls_for_level(level)
                food_spawn = True 
            else: 
                snake_pos.pop() 
 
            if food_spawn: 
                food = get_random_food() 
                food_spawn = False 
 
            current_time = pygame.time.get_ticks() 
            if current_time - food['spawn_time'] > 10000: 
                food_spawn = True 
 
        screen.fill(BLACK) 
        for pos in snake_pos: 
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10)) 
 
        food_color = RED if food['weight'] == 1 else (255, 165, 0) 
        pygame.draw.rect(screen, food_color, pygame.Rect(food['pos'][0], food['pos'][1], 10, 10)) 

        for wall in walls:
            pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(wall[0], wall[1], 10, 10)) 

        font = pygame.font.SysFont('arial', 20) 
        score_text = font.render(f"Score: {score} Level: {level}", True, WHITE) 
        screen.blit(score_text, [0, 0]) 
 
        if paused: 
            pause_text = font.render("Paused", True, WHITE) 
            screen.blit(pause_text, [SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2]) 
 
        pygame.display.flip() 
        game_speed = 10 + int(level * speed_increase)
        fps.tick(game_speed) 
except SystemExit: 
    pygame.quit()