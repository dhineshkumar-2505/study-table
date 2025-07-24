from flask import Flask, render_template_string, jsonify, request
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Sample data storage (in production, use a database)
daily_progress = {
    'monday': {'tasks': [False, False, False, False], 'date': None},
    'tuesday': {'tasks': [False, False, False, False], 'date': None},
    'wednesday': {'tasks': [False, False, False, False], 'date': None},
    'thursday': {'tasks': [False, False, False, False], 'date': None},
    'friday': {'tasks': [False, False, False, False], 'date': None},
    'saturday': {'tasks': [False, False, False, False], 'date': None},
    'sunday': {'tasks': [False, False, False, False], 'date': None}
}

motivational_quotes = [
    {"quote": "Success is the sum of small efforts, repeated day in and day out.", "author": "Robert Collier"},
    {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"quote": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"quote": "Education is the most powerful weapon which you can use to change the world.", "author": "Nelson Mandela"},
    {"quote": "The expert in anything was once a beginner.", "author": "Helen Hayes"},
    {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"}
]

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/quote')
def get_quote():
    return jsonify(random.choice(motivational_quotes))

@app.route('/api/progress', methods=['POST'])
def update_progress():
    data = request.json
    day = data.get('day')
    task_index = data.get('task_index')
    completed = data.get('completed')
    
    if day in daily_progress:
        daily_progress[day]['tasks'][task_index] = completed
        daily_progress[day]['date'] = datetime.now().strftime('%Y-%m-%d')
    
    return jsonify({'success': True})

@app.route('/api/progress/<day>')
def get_progress(day):
    return jsonify(daily_progress.get(day, {'tasks': [False, False, False, False], 'date': None}))

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mathu's Premium Study Tracker</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            --warning-gradient: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
            --accent-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            --dark-gradient: linear-gradient(135deg, #232526 0%, #414345 100%);
            
            --glass-bg: rgba(255, 255, 255, 0.25);
            --glass-border: rgba(255, 255, 255, 0.18);
            --shadow-light: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            --shadow-heavy: 0 15px 35px rgba(0, 0, 0, 0.1);
            
            --text-primary: #2d3748;
            --text-secondary: #4a5568;
            --text-muted: #718096;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: float 6s ease-in-out infinite;
        }

        .particle:nth-child(1) { left: 10%; animation-delay: 0s; }
        .particle:nth-child(2) { left: 20%; animation-delay: 1s; }
        .particle:nth-child(3) { left: 30%; animation-delay: 2s; }
        .particle:nth-child(4) { left: 40%; animation-delay: 3s; }
        .particle:nth-child(5) { left: 50%; animation-delay: 4s; }
        .particle:nth-child(6) { left: 60%; animation-delay: 5s; }
        .particle:nth-child(7) { left: 70%; animation-delay: 6s; }
        .particle:nth-child(8) { left: 80%; animation-delay: 7s; }
        .particle:nth-child(9) { left: 90%; animation-delay: 8s; }

        @keyframes float {
            0%, 100% { transform: translateY(100vh) scale(0); }
            10%, 90% { opacity: 1; }
            50% { transform: translateY(-10vh) scale(1); }
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
            z-index: 2;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 40px 0;
        }

        .main-title {
            font-family: 'Playfair Display', serif;
            font-size: 4rem;
            font-weight: 700;
            background: linear-gradient(45deg, #fff, #f0f8ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 4px 20px rgba(0,0,0,0.3);
            margin-bottom: 15px;
            animation: titleGlow 3s ease-in-out infinite alternate;
        }

        @keyframes titleGlow {
            from { filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.5)); }
            to { filter: drop-shadow(0 0 40px rgba(255, 255, 255, 0.8)); }
        }

        .subtitle {
            font-size: 1.5rem;
            color: rgba(255, 255, 255, 0.9);
            font-weight: 300;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 20px;
            border: 1px solid var(--glass-border);
            box-shadow: var(--shadow-light);
            padding: 30px;
            margin: 20px 0;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .glass-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s ease;
        }

        .glass-card:hover::before {
            left: 100%;
        }

        .glass-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }

        .quote-section {
            text-align: center;
            margin-bottom: 40px;
        }

        .quote-text {
            font-size: 1.8rem;
            font-style: italic;
            color: white;
            margin-bottom: 15px;
            line-height: 1.6;
            font-weight: 300;
        }

        .quote-author {
            font-size: 1.2rem;
            color: rgba(255, 255, 255, 0.8);
            font-weight: 500;
        }

        .refresh-quote-btn {
            background: var(--accent-gradient);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            margin-top: 20px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        .refresh-quote-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        .timetable-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 40px;
        }

        .timetable-card {
            position: relative;
        }

        .timetable-header {
            font-family: 'Playfair Display', serif;
            font-size: 2.2rem;
            font-weight: 600;
            text-align: center;
            margin-bottom: 25px;
            color: white;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }

        .schedule-item {
            display: flex;
            align-items: center;
            padding: 20px;
            margin: 15px 0;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            border-left: 6px solid;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }

        .schedule-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.6s ease;
        }

        .schedule-item:hover::before {
            left: 100%;
        }

        .schedule-item:hover {
            transform: translateX(15px) scale(1.02);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .study-session { border-color: #e53e3e; }
        .dinner { border-color: #38b2ac; }
        .revision { border-color: #3182ce; }
        .morning { border-color: #d69e2e; }
        .evening { border-color: #9f7aea; }
        .night { border-color: #4299e1; }

        .time-slot {
            font-weight: 700;
            font-size: 1.1rem;
            color: var(--text-primary);
            min-width: 160px;
            padding: 8px 15px;
            background: linear-gradient(45deg, #f7fafc, #edf2f7);
            border-radius: 10px;
            border: 1px solid #e2e8f0;
        }

        .activity-name {
            font-size: 1.2rem;
            color: var(--text-secondary);
            margin-left: 20px;
            font-weight: 500;
            flex: 1;
        }

        .activity-icon {
            font-size: 1.5rem;
            margin-right: 15px;
        }

        .days-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin: 40px 0;
        }

        .day-card {
            position: relative;
            border-radius: 20px;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .day-header {
            background: var(--primary-gradient);
            color: white;
            padding: 25px;
            cursor: pointer;
            font-size: 1.4rem;
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .day-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s ease;
        }

        .day-header:hover::before {
            left: 100%;
        }

        .day-header:hover {
            background: var(--secondary-gradient);
            transform: scale(1.02);
        }

        .day-name {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .day-emoji {
            font-size: 1.8rem;
        }

        .expand-icon {
            font-size: 1.2rem;
            transition: transform 0.3s ease;
        }

        .expand-icon.rotated {
            transform: rotate(180deg);
        }

        .day-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
        }

        .day-content.active {
            max-height: 500px;
        }

        .task-list {
            padding: 25px;
        }

        .task-item {
            display: flex;
            align-items: center;
            padding: 18px;
            margin: 12px 0;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 12px;
            border-left: 4px solid #4299e1;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
        }

        .task-item:hover {
            transform: translateX(8px);
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            background: rgba(255, 255, 255, 1);
        }

        .task-checkbox {
            width: 24px;
            height: 24px;
            margin-right: 15px;
            cursor: pointer;
            accent-color: #4299e1;
            transform: scale(1.2);
        }

        .task-label {
            font-size: 1.1rem;
            color: var(--text-primary);
            cursor: pointer;
            flex: 1;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .task-completed {
            text-decoration: line-through;
            color: var(--text-muted);
            opacity: 0.7;
        }

        .progress-bar {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 4px;
            margin-top: 15px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: var(--success-gradient);
            border-radius: 4px;
            transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
        }

        .progress-fill::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
            background-image: linear-gradient(
                -45deg,
                rgba(255, 255, 255, .2) 25%,
                transparent 25%,
                transparent 50%,
                rgba(255, 255, 255, .2) 50%,
                rgba(255, 255, 255, .2) 75%,
                transparent 75%,
                transparent
            );
            background-size: 50px 50px;
            animation: move 2s linear infinite;
        }

        @keyframes move {
            0% { background-position: 0 0; }
            100% { background-position: 50px 50px; }
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin: 40px 0;
        }

        .stat-card {
            text-align: center;
            padding: 30px;
            border-radius: 20px;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .stat-card:nth-child(1) { background: var(--primary-gradient); }
        .stat-card:nth-child(2) { background: var(--secondary-gradient); }
        .stat-card:nth-child(3) { background: var(--success-gradient); }
        .stat-card:nth-child(4) { background: var(--warning-gradient); }

        .stat-card:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 900;
            color: white;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
            margin-bottom: 10px;
        }

        .stat-label {
            font-size: 1.1rem;
            color: rgba(255, 255, 255, 0.9);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .footer {
            text-align: center;
            margin-top: 60px;
            padding: 40px;
            border-radius: 20px;
        }

        .footer-message {
            font-size: 1.6rem;
            color: white;
            font-weight: 500;
            margin-bottom: 15px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }

        .footer-signature {
            font-size: 1.2rem;
            color: rgba(255, 255, 255, 0.8);
            font-style: italic;
        }

        .celebration {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 4rem;
            z-index: 1000;
            pointer-events: none;
            animation: celebrate 3s ease-out forwards;
        }

        @keyframes celebrate {
            0% { opacity: 0; transform: translate(-50%, -50%) scale(0) rotate(0deg); }
            50% { opacity: 1; transform: translate(-50%, -50%) scale(1.5) rotate(180deg); }
            100% { opacity: 0; transform: translate(-50%, -50%) scale(1) rotate(360deg); }
        }

        .floating-action-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: var(--accent-gradient);
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            z-index: 1000;
        }

        .floating-action-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 25px rgba(0,0,0,0.4);
        }

        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            
            .timetable-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .days-container {
                grid-template-columns: 1fr;
            }
            
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .container {
                padding: 15px;
            }
        }

        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255,255,255,.3);
            border-radius: 50%;
            border-top-color: #fff;
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 12px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, #667eea, #764ba2);
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, #764ba2, #667eea);
        }
    </style>
</head>
<body>
    <div class="particles">
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
    </div>

    <div class="container">
        <header class="header">
            <h1 class="main-title">✨ Madhu's Study Tracker ✨</h1>
            <p class="subtitle">Excellence Through Consistency</p>
        </header>

        <div class="glass-card quote-section">
            <div class="quote-text" id="quote-text">
                "Success is the sum of small efforts, repeated day in and day out."
            </div>
            <div class="quote-author" id="quote-author">- Robert Collier</div>
            <button class="refresh-quote-btn" onclick="refreshQuote()">
                <i class="fas fa-sync-alt"></i> New Inspiration
            </button>
        </div>

        <div class="timetable-grid">
            <div class="glass-card timetable-card">
                <h2 class="timetable-header">
                    <i class="fas fa-calendar-week"></i> Weekdays Schedule
                </h2>
                
                <div class="schedule-item study-session">
                    <div class="activity-icon">📚</div>
                    <div class="time-slot">6:00 PM – 7:30 PM</div>
                    <div class="activity-name">Deep Focus Study Session</div>
                </div>
                
                <div class="schedule-item dinner">
                    <div class="activity-icon">🍽️</div>
                    <div class="time-slot">7:30 PM – 8:30 PM</div>
                    <div class="activity-name">Nourishment Break</div>
                </div>
                
                <div class="schedule-item study-session">
                    <div class="activity-icon">📖</div>
                    <div class="time-slot">8:30 PM – 10:00 PM</div>
                    <div class="activity-name">Intensive Study Session</div>
                </div>
                
                <div class="schedule-item revision">
                    <div class="activity-icon">🔄</div>
                    <div class="time-slot">10:00 PM – 10:30 PM</div>
                    <div class="activity-name">Knowledge Consolidation</div>
                </div>
            </div>

            <div class="glass-card timetable-card">
                <h2 class="timetable-header">
                    <i class="fas fa-sun"></i> Sunday Special
                </h2>
                
                <div class="schedule-item morning">
                    <div class="activity-icon">🌅</div>
                    <div class="time-slot">10:00 AM – 11:30 AM</div>
                    <div class="activity-name">Morning Clarity Session</div>
                </div>
                
                <div class="schedule-item evening">
                    <div class="activity-icon">🌆</div>
                    <div class="time-slot">6:00 PM – 8:30 PM</div>
                    <div class="activity-name">Extended Study Marathon</div>
                </div>
                
                <div class="schedule-item dinner">
                    <div class="activity-icon">🍽️</div>
                    <div class="time-slot">8:30 PM – 9:30 PM</div>
                    <div class="activity-name">Mindful Dining</div>
                </div>
                
                <div class="schedule-item night">
                    <div class="activity-icon">🌙</div>
                    <div class="time-slot">9:30 PM – 10:30 PM</div>
                    <div class="activity-name">Reflective Review</div>
                </div>
            </div>
        </div>

        <div class="stats-grid">
            <div class="stat-card glass-card">
                <div class="stat-number" id="total-tasks">0</div>
                <div class="stat-label">Tasks Completed</div>
            </div>
            <div class="stat-card glass-card">
                <div class="stat-number" id="completion-rate">0%</div>
                <div class="stat-label">Success Rate</div>
            </div>
            <div class="stat-card glass-card">
                <div class="stat-number" id="streak-count">0</div>
                <div class="stat-label">Day Streak</div>
            </div>
            <div class="stat-card glass-card">
                <div class="stat-number" id="weekly-progress">0%</div>
                <div class="stat-label">Weekly Progress</div>
            </div>
        </div>

        <div class="days-container">
            <!-- Monday -->
            <div class="day-card glass-card">
                <div class="day-header" onclick="toggleDay('monday')">
                    <div class="day-name">
                        <span class="day-emoji">🌟</span>
                        <span>Monday - Fresh Start</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="monday-icon"></i>
                </div>
                <div class="day-content" id="monday-content">
                    <div class="task-list">
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="mon-task-0" onchange="updateTaskProgress('monday', 0, this.checked)">
                            <label class="task-label" for="mon-task-0">Complete Deep Focus Study Session (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="mon-task-1" onchange="updateTaskProgress('monday', 1, this.checked)">
                            <label class="task-label" for="mon-task-1">Complete Intensive Study Session (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="mon-task-2" onchange="updateTaskProgress('monday', 2, this.checked)">
                            <label class="task-label" for="mon-task-2">Complete Knowledge Consolidation (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="mon-task-3" onchange="updateTaskProgress('monday', 3, this.checked)">
                            <label class="task-label" for="mon-task-3">Maintain positive mindset and motivation</label>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="monday-progress" style="width: 0%"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Tuesday -->
            <div class="day-card glass-card">
                <div class="day-header" onclick="toggleDay('tuesday')">
                    <div class="day-name">
                        <span class="day-emoji">🔥</span>
                        <span>Tuesday - Power Day</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="tuesday-icon"></i>
                </div>
                <div class="day-content" id="tuesday-content">
                    <div class="task-list">
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="tue-task-0" onchange="updateTaskProgress('tuesday', 0, this.checked)">
                            <label class="task-label" for="tue-task-0">Complete Deep Focus Study Session (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="tue-task-1" onchange="updateTaskProgress('tuesday', 1, this.checked)">
                            <label class="task-label" for="tue-task-1">Complete Intensive Study Session (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="tue-task-2" onchange="updateTaskProgress('tuesday', 2, this.checked)">
                            <label class="task-label" for="tue-task-2">Complete Knowledge Consolidation (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="tue-task-3" onchange="updateTaskProgress('tuesday', 3, this.checked)">
                            <label class="task-label" for="tue-task-3">Maintain positive mindset and motivation</label>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="tuesday-progress" style="width: 0%"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Wednesday -->
            <div class="day-card glass-card">
                <div class="day-header" onclick="toggleDay('wednesday')">
                    <div class="day-name">
                        <span class="day-emoji">🚀</span>
                        <span>Wednesday - Momentum</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="wednesday-icon"></i>
                </div>
                <div class="day-content" id="wednesday-content">
                    <div class="task-list">
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="wed-task-0" onchange="updateTaskProgress('wednesday', 0, this.checked)">
                            <label class="task-label" for="wed-task-0">Complete Deep Focus Study Session (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="wed-task-1" onchange="updateTaskProgress('wednesday', 1, this.checked)">
                            <label class="task-label" for="wed-task-1">Complete Intensive Study Session (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="wed-task-2" onchange="updateTaskProgress('wednesday', 2, this.checked)">
                            <label class="task-label" for="wed-task-2">Complete Knowledge Consolidation (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="wed-task-3" onchange="updateTaskProgress('wednesday', 3, this.checked)">
                            <label class="task-label" for="wed-task-3">Maintain positive mindset and motivation</label>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="wednesday-progress" style="width: 0%"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Thursday -->
            <div class="day-card glass-card">
                <div class="day-header" onclick="toggleDay('thursday')">
                    <div class="day-name">
                        <span class="day-emoji">⚡</span>
                        <span>Thursday - Excellence</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="thursday-icon"></i>
                </div>
                <div class="day-content" id="thursday-content">
                    <div class="task-list">
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="thu-task-0" onchange="updateTaskProgress('thursday', 0, this.checked)">
                            <label class="task-label" for="thu-task-0">Complete Deep Focus Study Session (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="thu-task-1" onchange="updateTaskProgress('thursday', 1, this.checked)">
                            <label class="task-label" for="thu-task-1">Complete Intensive Study Session (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="thu-task-2" onchange="updateTaskProgress('thursday', 2, this.checked)">
                            <label class="task-label" for="thu-task-2">Complete Knowledge Consolidation (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="thu-task-3" onchange="updateTaskProgress('thursday', 3, this.checked)">
                            <label class="task-label" for="thu-task-3">Maintain positive mindset and motivation</label>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="thursday-progress" style="width: 0%"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Friday -->
            <div class="day-card glass-card">
                <div class="day-header" onclick="toggleDay('friday')">
                    <div class="day-name">
                        <span class="day-emoji">🎯</span>
                        <span>Friday - Victory</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="friday-icon"></i>
                </div>
                <div class="day-content" id="friday-content">
                    <div class="task-list">
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="fri-task-0" onchange="updateTaskProgress('friday', 0, this.checked)">
                            <label class="task-label" for="fri-task-0">Complete Deep Focus Study Session (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="fri-task-1" onchange="updateTaskProgress('friday', 1, this.checked)">
                            <label class="task-label" for="fri-task-1">Complete Intensive Study Session (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="fri-task-2" onchange="updateTaskProgress('friday', 2, this.checked)">
                            <label class="task-label" for="fri-task-2">Complete Knowledge Consolidation (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="fri-task-3" onchange="updateTaskProgress('friday', 3, this.checked)">
                            <label class="task-label" for="fri-task-3">Maintain positive mindset and motivation</label>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="friday-progress" style="width: 0%"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Saturday -->
            <div class="day-card glass-card">
                <div class="day-header" onclick="toggleDay('saturday')">
                    <div class="day-name">
                        <span class="day-emoji">💎</span>
                        <span>Saturday - Diamond</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="saturday-icon"></i>
                </div>
                <div class="day-content" id="saturday-content">
                    <div class="task-list">
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="sat-task-0" onchange="updateTaskProgress('saturday', 0, this.checked)">
                            <label class="task-label" for="sat-task-0">Complete Deep Focus Study Session (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="sat-task-1" onchange="updateTaskProgress('saturday', 1, this.checked)">
                            <label class="task-label" for="sat-task-1">Complete Intensive Study Session (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="sat-task-2" onchange="updateTaskProgress('saturday', 2, this.checked)">
                            <label class="task-label" for="sat-task-2">Complete Knowledge Consolidation (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="sat-task-3" onchange="updateTaskProgress('saturday', 3, this.checked)">
                            <label class="task-label" for="sat-task-3">Maintain positive mindset and motivation</label>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="saturday-progress" style="width: 0%"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Sunday -->
            <div class="day-card glass-card">
                <div class="day-header" onclick="toggleDay('sunday')">
                    <div class="day-name">
                        <span class="day-emoji">🌟</span>
                        <span>Sunday - Mastery</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="sunday-icon"></i>
                </div>
                <div class="day-content" id="sunday-content">
                    <div class="task-list">
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="sun-task-0" onchange="updateTaskProgress('sunday', 0, this.checked)">
                            <label class="task-label" for="sun-task-0">Complete Morning Clarity Session (10:00-11:30 AM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="sun-task-1" onchange="updateTaskProgress('sunday', 1, this.checked)">
                            <label class="task-label" for="sun-task-1">Complete Extended Study Marathon (6:00-8:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="sun-task-2" onchange="updateTaskProgress('sunday', 2, this.checked)">
                            <label class="task-label" for="sun-task-2">Complete Reflective Review (9:30-10:30 PM)</label>
                        </div>
                        <div class="task-item">
                            <input type="checkbox" class="task-checkbox" id="sun-task-3" onchange="updateTaskProgress('sunday', 3, this.checked)">
                            <label class="task-label" for="sun-task-3">Prepare and strategize for the upcoming week</label>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="sunday-progress" style="width: 0%"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="glass-card footer">
            <div class="footer-message">
                <i class="fas fa-heart" style="color: #ff6b6b;"></i>
                "Every small step today creates tomorrow's success story"
                <i class="fas fa-star" style="color: #feca57;"></i>
            </div>
            <div class="footer-signature">
                Crafted with love for Mathu's academic excellence ✨
            </div>
        </div>
    </div>

    <button class="floating-action-btn" onclick="scrollToTop()" title="Back to Top">
        <i class="fas fa-arrow-up"></i>
    </button>

    <script>
        let dailyData = {
            monday: [false, false, false, false],
            tuesday: [false, false, false, false],
            wednesday: [false, false, false, false],
            thursday: [false, false, false, false],
            friday: [false, false, false, false],
            saturday: [false, false, false, false],
            sunday: [false, false, false, false]
        };

        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            loadProgressData();
            updateAllStats();
            refreshQuote();
            
            // Load saved progress from localStorage (if available)
            const savedData = localStorage.getItem('mathuStudyTracker');
            if (savedData) {
                try {
                    dailyData = JSON.parse(savedData);
                    loadCheckboxStates();
                    updateAllProgressBars();
                    updateAllStats();
                } catch (e) {
                    console.log('Could not load saved data');
                }
            }
        });

        // Toggle day section visibility
        function toggleDay(day) {
            const content = document.getElementById(day + '-content');
            const icon = document.getElementById(day + '-icon');
            
            if (content.classList.contains('active')) {
                content.classList.remove('active');
                icon.classList.remove('rotated');
            } else {
                content.classList.add('active');
                icon.classList.add('rotated');
            }
        }

        // Update task progress
        function updateTaskProgress(day, taskIndex, completed) {
            dailyData[day][taskIndex] = completed;
            
            // Update visual feedback
            const label = document.querySelector(`label[for="${getTaskId(day, taskIndex)}"]`);
            if (completed) {
                label.classList.add('task-completed');
                showCelebration();
            } else {
                label.classList.remove('task-completed');
            }
            
            // Update progress bar for the day
            updateProgressBar(day);
            
            // Update overall statistics
            updateAllStats();
            
            // Save progress
            saveProgressData();
            
            // Send to backend
            fetch('/api/progress', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    day: day,
                    task_index: taskIndex,
                    completed: completed
                })
            });
        }

        // Get task ID helper
        function getTaskId(day, taskIndex) {
            const dayPrefixes = {
                monday: 'mon',
                tuesday: 'tue',
                wednesday: 'wed',
                thursday: 'thu',
                friday: 'fri',
                saturday: 'sat',
                sunday: 'sun'
            };
            return `${dayPrefixes[day]}-task-${taskIndex}`;
        }

        // Update progress bar for a specific day
        function updateProgressBar(day) {
            const completedTasks = dailyData[day].filter(task => task).length;
            const totalTasks = dailyData[day].length;
            const percentage = (completedTasks / totalTasks) * 100;
            
            const progressBar = document.getElementById(day + '-progress');
            if (progressBar) {
                progressBar.style.width = percentage + '%';
            }
        }

        // Update all progress bars
        function updateAllProgressBars() {
            Object.keys(dailyData).forEach(day => {
                updateProgressBar(day);
            });
        }

        // Update all statistics
        function updateAllStats() {
            let totalTasks = 0;
            let completedTasks = 0;
            let completedDays = 0;
            
            Object.keys(dailyData).forEach(day => {
                const dayTasks = dailyData[day];
                const dayCompleted = dayTasks.filter(task => task).length;
                
                totalTasks += dayTasks.length;
                completedTasks += dayCompleted;
                
                if (dayCompleted === dayTasks.length) {
                    completedDays++;
                }
            });
            
            const completionRate = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;
            const weeklyProgress = Math.round((completedDays / 7) * 100);
            
            // Update DOM elements
            document.getElementById('total-tasks').textContent = completedTasks;
            document.getElementById('completion-rate').textContent = completionRate + '%';
            document.getElementById('streak-count').textContent = calculateStreak();
            document.getElementById('weekly-progress').textContent = weeklyProgress + '%';
        }

        // Calculate streak
        function calculateStreak() {
            const days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
            let streak = 0;
            
            for (let i = days.length - 1; i >= 0; i--) {
                const day = days[i];
                const completedTasks = dailyData[day].filter(task => task).length;
                const totalTasks = dailyData[day].length;
                
                if (completedTasks === totalTasks) {
                    streak++;
                } else {
                    break;
                }
            }
            
            return streak;
        }

        // Load checkbox states
        function loadCheckboxStates() {
            Object.keys(dailyData).forEach(day => {
                dailyData[day].forEach((completed, index) => {
                    const checkbox = document.getElementById(getTaskId(day, index));
                    const label = document.querySelector(`label[for="${getTaskId(day, index)}"]`);
                    
                    if (checkbox) {
                        checkbox.checked = completed;
                        if (completed) {
                            label.classList.add('task-completed');
                        } else {
                            label.classList.remove('task-completed');
                        }
                    }
                });
            });
        }

        // Save progress data
        function saveProgressData() {
            try {
                localStorage.setItem('mathuStudyTracker', JSON.stringify(dailyData));
            } catch (e) {
                console.log('Could not save progress data');
            }
        }

        // Load progress data
        function loadProgressData() {
            // This would typically load from backend
            // For now, we'll use localStorage as fallback
        }

        // Refresh motivational quote
        async function refreshQuote() {
            const button = document.querySelector('.refresh-quote-btn');
            const originalText = button.innerHTML;
            button.innerHTML = '<div class="loading"></div> Loading...';
            
            try {
                const response = await fetch('/api/quote');
                const data = await response.json();
                
                document.getElementById('quote-text').textContent = `"${data.quote}"`;
                document.getElementById('quote-author').textContent = `- ${data.author}`;
                
                // Add animation
                const quoteElement = document.getElementById('quote-text');
                quoteElement.style.opacity = '0';
                setTimeout(() => {
                    quoteElement.style.opacity = '1';
                }, 300);
                
            } catch (error) {
                console.error('Error fetching quote:', error);
            } finally {
                button.innerHTML = originalText;
            }
        }

        // Show celebration animation
        function showCelebration() {
            const celebration = document.createElement('div');
            celebration.className = 'celebration';
            celebration.textContent = '🎉✨🌟';
            document.body.appendChild(celebration);
            
            setTimeout(() => {
                document.body.removeChild(celebration);
            }, 3000);
        }

        // Scroll to top
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }

        // Add smooth scroll behavior to all internal links
        document.addEventListener('click', function(e) {
            if (e.target.tagName === 'A' && e.target.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(e.target.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });

        // Add keyboard shortcuts
        document.addEventListener('keydown', function(e) {
            // Ctrl + R to refresh quote
            if (e.ctrlKey && e.key === 'r') {
                e.preventDefault();
                refreshQuote();
            }
            
            // Escape to close all expanded days
            if (e.key === 'Escape') {
                document.querySelectorAll('.day-content.active').forEach(content => {
                    content.classList.remove('active');
                });
                document.querySelectorAll('.expand-icon.rotated').forEach(icon => {
                    icon.classList.remove('rotated');
                });
            }
        });

        // Add intersection observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe all cards for animation
        document.addEventListener('DOMContentLoaded', () => {
            document.querySelectorAll('.glass-card, .day-card').forEach(card => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                observer.observe(card);
            });
        });

        // Add periodic auto-save
        setInterval(() => {
            saveProgressData();
        }, 30000); // Save every 30 seconds

        // Handle page visibility change
        document.addEventListener('visibilitychange', () => {
            if (!document.hidden) {
                // Page became visible, refresh data
                updateAllStats();
            }
        });

        // Add touch support for mobile
        let touchStartY = 0;
        let touchEndY = 0;

        document.addEventListener('touchstart', (e) => {
            touchStartY = e.changedTouches[0].screenY;
        }, false);

        document.addEventListener('touchend', (e) => {
            touchEndY = e.changedTouches[0].screenY;
            handleSwipe();
        }, false);

        function handleSwipe() {
            const swipeThreshold = 50;
            const diff = touchStartY - touchEndY;
            
            if (Math.abs(diff) > swipeThreshold) {
                if (diff > 0) {
                    // Swipe up - could trigger some action
                    console.log('Swipe up detected');
                } else {
                    // Swipe down - could trigger refresh
                    console.log('Swipe down detected');
                }
            }
        }
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)