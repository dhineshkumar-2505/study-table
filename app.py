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
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>Mathu's Mobile Study Tracker</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --primary-color: #667eea;
            --secondary-color: #764ba2;
            --accent-color: #f093fb;
            --success-color: #4facfe;
            --warning-color: #43e97b;
            --danger-color: #f5576c;
            
            --glass-bg: rgba(255, 255, 255, 0.15);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-light: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
            --shadow-heavy: 0 4px 20px rgba(0, 0, 0, 0.1);
            
            --text-primary: #2d3748;
            --text-secondary: #4a5568;
            --text-light: #ffffff;
            
            --border-radius: 16px;
            --spacing-xs: 8px;
            --spacing-sm: 12px;
            --spacing-md: 16px;
            --spacing-lg: 24px;
            --spacing-xl: 32px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
            font-size: 16px;
            line-height: 1.5;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .container {
            max-width: 100%;
            margin: 0 auto;
            padding: var(--spacing-md);
            position: relative;
            z-index: 2;
        }

        /* Mobile-first header */
        .header {
            text-align: center;
            margin-bottom: var(--spacing-lg);
            padding: var(--spacing-lg) 0;
        }

        .main-title {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, #fff, #f0f8ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 4px 20px rgba(0,0,0,0.3);
            margin-bottom: var(--spacing-sm);
            animation: titleGlow 3s ease-in-out infinite alternate;
        }

        @keyframes titleGlow {
            from { filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.4)); }
            to { filter: drop-shadow(0 0 25px rgba(255, 255, 255, 0.6)); }
        }

        .subtitle {
            font-size: 1rem;
            color: rgba(255, 255, 255, 0.9);
            font-weight: 400;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        /* Mobile-optimized glass cards */
        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: var(--border-radius);
            border: 1px solid var(--glass-border);
            box-shadow: var(--shadow-light);
            padding: var(--spacing-lg);
            margin: var(--spacing-md) 0;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        /* Mobile quote section */
        .quote-section {
            text-align: center;
            margin-bottom: var(--spacing-lg);
        }

        .quote-text {
            font-size: 1.3rem;
            font-style: italic;
            color: white;
            margin-bottom: var(--spacing-sm);
            line-height: 1.4;
            font-weight: 300;
        }

        .quote-author {
            font-size: 1rem;
            color: rgba(255, 255, 255, 0.8);
            font-weight: 500;
            margin-bottom: var(--spacing-md);
        }

        .refresh-quote-btn {
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            color: white;
            border: none;
            padding: var(--spacing-md) var(--spacing-lg);
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: var(--shadow-heavy);
            min-height: 48px;
            min-width: 140px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: var(--spacing-xs);
            margin: 0 auto;
        }

        .refresh-quote-btn:active {
            transform: scale(0.95);
        }

        /* Mobile stats grid */
        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--spacing-md);
            margin: var(--spacing-lg) 0;
        }

        .stat-card {
            text-align: center;
            padding: var(--spacing-lg);
            border-radius: var(--border-radius);
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
            min-height: 100px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .stat-card:nth-child(1) { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .stat-card:nth-child(2) { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
        .stat-card:nth-child(3) { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
        .stat-card:nth-child(4) { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }

        .stat-number {
            font-size: 2rem;
            font-weight: 900;
            color: white;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
            margin-bottom: var(--spacing-xs);
        }

        .stat-label {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.9);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* Mobile-first day cards */
        .days-container {
            margin: var(--spacing-lg) 0;
        }

        .day-card {
            margin: var(--spacing-md) 0;
            border-radius: var(--border-radius);
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .day-header {
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            padding: var(--spacing-lg);
            cursor: pointer;
            font-size: 1.2rem;
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            min-height: 60px;
            user-select: none;
        }

        .day-header:active {
            background: linear-gradient(135deg, var(--accent-color) 0%, var(--danger-color) 100%);
            transform: scale(0.98);
        }

        .day-name {
            display: flex;
            align-items: center;
            gap: var(--spacing-sm);
        }

        .day-emoji {
            font-size: 1.5rem;
        }

        .expand-icon {
            font-size: 1.1rem;
            transition: transform 0.3s ease;
        }

        .expand-icon.rotated {
            transform: rotate(180deg);
        }

        .day-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
        }

        .day-content.active {
            max-height: 600px;
        }

        .task-list {
            padding: var(--spacing-lg);
        }

        /* Mobile-optimized task items */
        .task-item {
            display: flex;
            align-items: center;
            padding: var(--spacing-lg);
            margin: var(--spacing-sm) 0;
            background: rgba(255, 255, 255, 0.9);
            border-radius: var(--border-radius);
            border-left: 4px solid #4299e1;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            min-height: 60px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .task-item:active {
            transform: scale(0.98);
            background: rgba(255, 255, 255, 1);
        }

        .task-checkbox {
            width: 24px;
            height: 24px;
            margin-right: var(--spacing-md);
            cursor: pointer;
            accent-color: #4299e1;
            transform: scale(1.2);
            flex-shrink: 0;
        }

        .task-label {
            font-size: 1rem;
            color: var(--text-primary);
            cursor: pointer;
            flex: 1;
            font-weight: 500;
            transition: all 0.3s ease;
            line-height: 1.4;
        }

        .task-completed {
            text-decoration: line-through;
            color: var(--text-secondary);
            opacity: 0.7;
        }

        .progress-bar {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 4px;
            margin-top: var(--spacing-md);
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
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
            background-size: 30px 30px;
            animation: move 2s linear infinite;
        }

        @keyframes move {
            0% { background-position: 0 0; }
            100% { background-position: 30px 30px; }
        }

        /* Mobile schedule section */
        .schedule-section {
            margin: var(--spacing-lg) 0;
        }

        .schedule-header {
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            font-weight: 600;
            text-align: center;
            margin-bottom: var(--spacing-lg);
            color: white;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }

        .schedule-tabs {
            display: flex;
            background: rgba(255, 255, 255, 0.2);
            border-radius: var(--border-radius);
            margin-bottom: var(--spacing-lg);
            overflow: hidden;
        }

        .schedule-tab {
            flex: 1;
            padding: var(--spacing-md);
            background: transparent;
            border: none;
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            min-height: 50px;
        }

        .schedule-tab.active {
            background: rgba(255, 255, 255, 0.3);
        }

        .schedule-tab:active {
            transform: scale(0.95);
        }

        .schedule-content {
            display: none;
        }

        .schedule-content.active {
            display: block;
        }

        .schedule-item {
            display: flex;
            align-items: center;
            padding: var(--spacing-lg);
            margin: var(--spacing-sm) 0;
            background: rgba(255, 255, 255, 0.9);
            border-radius: var(--border-radius);
            border-left: 6px solid;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            min-height: 70px;
        }

        .study-session { border-color: #e53e3e; }
        .dinner { border-color: #38b2ac; }
        .revision { border-color: #3182ce; }
        .morning { border-color: #d69e2e; }
        .evening { border-color: #9f7aea; }
        .night { border-color: #4299e1; }

        .time-slot {
            font-weight: 700;
            font-size: 0.9rem;
            color: var(--text-primary);
            min-width: 120px;
            padding: var(--spacing-xs) var(--spacing-sm);
            background: linear-gradient(45deg, #f7fafc, #edf2f7);
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            text-align: center;
            flex-shrink: 0;
        }

        .activity-name {
            font-size: 1rem;
            color: var(--text-secondary);
            margin-left: var(--spacing-md);
            font-weight: 500;
            flex: 1;
            line-height: 1.3;
        }

        .activity-icon {
            font-size: 1.3rem;
            margin-right: var(--spacing-sm);
            flex-shrink: 0;
        }

        /* Mobile footer */
        .footer {
            text-align: center;
            margin-top: var(--spacing-xl);
            padding: var(--spacing-xl);
            border-radius: var(--border-radius);
        }

        .footer-message {
            font-size: 1.3rem;
            color: white;
            font-weight: 500;
            margin-bottom: var(--spacing-sm);
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }

        .footer-signature {
            font-size: 1rem;
            color: rgba(255, 255, 255, 0.8);
            font-style: italic;
        }

        /* Mobile celebration */
        .celebration {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 3rem;
            z-index: 1000;
            pointer-events: none;
            animation: celebrate 2s ease-out forwards;
        }

        @keyframes celebrate {
            0% { opacity: 0; transform: translate(-50%, -50%) scale(0) rotate(0deg); }
            50% { opacity: 1; transform: translate(-50%, -50%) scale(1.2) rotate(180deg); }
            100% { opacity: 0; transform: translate(-50%, -50%) scale(1) rotate(360deg); }
        }

        /* Mobile floating button */
        .floating-buttons {
            position: fixed;
            bottom: var(--spacing-lg);
            right: var(--spacing-lg);
            display: flex;
            flex-direction: column;
            gap: var(--spacing-sm);
            z-index: 1000;
        }

        .floating-btn {
            width: 56px;
            height: 56px;
            border-radius: 50%;
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            border: none;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            box-shadow: 0 4px 16px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .floating-btn:active {
            transform: scale(0.9);
        }

        /* Loading spinner */
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

        /* Mobile pull-to-refresh indicator */
        .pull-to-refresh {
            position: fixed;
            top: -60px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.9);
            padding: var(--spacing-md) var(--spacing-lg);
            border-radius: 0 0 var(--border-radius) var(--border-radius);
            box-shadow: var(--shadow-light);
            transition: top 0.3s ease;
            z-index: 1000;
            font-weight: 600;
            color: var(--text-primary);
        }

        .pull-to-refresh.visible {
            top: 0;
        }

        /* Responsive adjustments */
        @media (max-width: 480px) {
            .container {
                padding: var(--spacing-sm);
            }
            
            .main-title {
                font-size: 2rem;
            }
            
            .quote-text {
                font-size: 1.1rem;
            }
            
            .stats-grid {
                gap: var(--spacing-sm);
            }
            
            .stat-number {
                font-size: 1.8rem;
            }
            
            .stat-label {
                font-size: 0.8rem;
            }
            
            .day-header {
                padding: var(--spacing-md);
                font-size: 1.1rem;
            }
            
            .task-item {
                padding: var(--spacing-md);
                min-height: 56px;
            }
            
            .task-label {
                font-size: 0.95rem;
            }
            
            .time-slot {
                min-width: 100px;
                font-size: 0.8rem;
            }
            
            .activity-name {
                font-size: 0.9rem;
            }
        }

        /* Landscape orientation adjustments */
        @media (orientation: landscape) and (max-height: 600px) {
            .header {
                padding: var(--spacing-md) 0;
                margin-bottom: var(--spacing-md);
            }
            
            .main-title {
                font-size: 2rem;
                margin-bottom: var(--spacing-xs);
            }
            
            .subtitle {
                font-size: 0.9rem;
            }
            
            .stats-grid {
                grid-template-columns: repeat(4, 1fr);
                gap: var(--spacing-sm);
            }
            
            .stat-card {
                padding: var(--spacing-md);
                min-height: 80px;
            }
            
            .stat-number {
                font-size: 1.5rem;
            }
        }

        /* Dark mode support */
        @media (prefers-color-scheme: dark) {
            .glass-card {
                background: rgba(0, 0, 0, 0.3);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
            
            .day-content {
                background: rgba(0, 0, 0, 0.7);
            }
            
            .task-item {
                background: rgba(255, 255, 255, 0.1);
                color: white;
            }
            
            .task-label {
                color: white;
            }
            
            .schedule-item {
                background: rgba(255, 255, 255, 0.1);
                color: white;
            }
            
            .time-slot {
                background: rgba(255, 255, 255, 0.2);
                color: white;
                border-color: rgba(255, 255, 255, 0.1);
            }
            
            .activity-name {
                color: rgba(255, 255, 255, 0.9);
            }
        }

        /* Accessibility improvements */
        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }

        /* High contrast support */
        @media (prefers-contrast: high) {
            .glass-card {
                background: rgba(255, 255, 255, 0.9);
                border: 2px solid #000;
            }
            
            .task-item {
                border: 2px solid #000;
            }
        }

        /* Focus indicators for keyboard navigation */
        button:focus-visible,
        input:focus-visible,
        .task-item:focus-visible {
            outline: 3px solid #4facfe;
            outline-offset: 2px;
        }

        /* Improved touch targets */
        .task-item,
        .day-header,
        .schedule-tab,
        .refresh-quote-btn,
        .floating-btn {
            touch-action: manipulation;
        }
    </style>
</head>
<body>
    <div class="pull-to-refresh" id="pullToRefresh">
        <i class="fas fa-arrow-down"></i> Release to refresh
    </div>

    <div class="container">
        <header class="header">
            <h1 class="main-title">✨ Mathu's Study Tracker ✨</h1>
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

        <div class="stats-grid">
            <div class="stat-card glass-card">
                <div class="stat-number" id="total-tasks">0</div>
                <div class="stat-label">Tasks Done</div>
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
                <div class="stat-label">Weekly Goal</div>
            </div>
        </div>

        <div class="glass-card schedule-section">
            <h2 class="schedule-header">
                <i class="fas fa-calendar-alt"></i> Study Schedule
            </h2>
            
            <div class="schedule-tabs">
                <button class="schedule-tab active" onclick="showSchedule('weekdays')">
                    Weekdays
                </button>
                <button class="schedule-tab" onclick="showSchedule('sunday')">
                    Sunday
                </button>
            </div>

            <div id="weekdays-schedule" class="schedule-content active">
                <div class="schedule-item study-session">
                    <div class="activity-icon">📚</div>
                    <div class="time-slot">6:00 - 7:30 PM</div>
                    <div class="activity-name">Deep Focus Study</div>
                </div>
                
                <div class="schedule-item dinner">
                    <div class="activity-icon">🍽️</div>
                    <div class="time-slot">7:30 - 8:30 PM</div>
                    <div class="activity-name">Dinner Break</div>
                </div>
                
                <div class="schedule-item study-session">
                    <div class="activity-icon">📖</div>
                    <div class="time-slot">8:30 - 10:00 PM</div>
                    <div class="activity-name">Intensive Study</div>
                </div>
                
                <div class="schedule-item revision">
                    <div class="activity-icon">🔄</div>
                    <div class="time-slot">10:00 - 10:30 PM</div>
                    <div class="activity-name">Quick Review</div>
                </div>
            </div>

            <div id="sunday-schedule" class="schedule-content">
                <div class="schedule-item morning">
                    <div class="activity-icon">🌅</div>
                    <div class="time-slot">10:00 - 11:30 AM</div>
                    <div class="activity-name">Morning Session</div>
                </div>
                
                <div class="schedule-item evening">
                    <div class="activity-icon">🌆</div>
                    <div class="time-slot">6:00 - 8:30 PM</div>
                    <div class="activity-name">Study Marathon</div>
                </div>
                
                <div class="schedule-item dinner">
                    <div class="activity-icon">🍽️</div>
                    <div class="time-slot">8:30 - 9:30 PM</div>
                    <div class="activity-name">Mindful Dining</div>
                </div>
                
                <div class="schedule-item night">
                    <div class="activity-icon">🌙</div>
                    <div class="time-slot">9:30 - 10:30 PM</div>
                    <div class="activity-name">Reflective Review</div>
                </div>
            </div>
        </div>

        <div class="days-container">
            <!-- Monday -->
            <div class="day-card glass-card">
                <div class="day-header" onclick="toggleDay('monday')">
                    <div class="day-name">
                        <span class="day-emoji">🌟</span>
                        <span>Monday</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="monday-icon"></i>
                </div>
                <div class="day-content" id="monday-content">
                    <div class="task-list">
                        <div class="task-item" onclick="toggleTask('monday', 0)">
                            <input type="checkbox" class="task-checkbox" id="mon-task-0" onchange="updateTaskProgress('monday', 0, this.checked)">
                            <label class="task-label" for="mon-task-0">Complete Deep Focus Study (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('monday', 1)">
                            <input type="checkbox" class="task-checkbox" id="mon-task-1" onchange="updateTaskProgress('monday', 1, this.checked)">
                            <label class="task-label" for="mon-task-1">Complete Intensive Study (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('monday', 2)">
                            <input type="checkbox" class="task-checkbox" id="mon-task-2" onchange="updateTaskProgress('monday', 2, this.checked)">
                            <label class="task-label" for="mon-task-2">Complete Review Session (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('monday', 3)">
                            <input type="checkbox" class="task-checkbox" id="mon-task-3" onchange="updateTaskProgress('monday', 3, this.checked)">
                            <label class="task-label" for="mon-task-3">Maintain positive mindset</label>
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
                        <span>Tuesday</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="tuesday-icon"></i>
                </div>
                <div class="day-content" id="tuesday-content">
                    <div class="task-list">
                        <div class="task-item" onclick="toggleTask('tuesday', 0)">
                            <input type="checkbox" class="task-checkbox" id="tue-task-0" onchange="updateTaskProgress('tuesday', 0, this.checked)">
                            <label class="task-label" for="tue-task-0">Complete Deep Focus Study (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('tuesday', 1)">
                            <input type="checkbox" class="task-checkbox" id="tue-task-1" onchange="updateTaskProgress('tuesday', 1, this.checked)">
                            <label class="task-label" for="tue-task-1">Complete Intensive Study (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('tuesday', 2)">
                            <input type="checkbox" class="task-checkbox" id="tue-task-2" onchange="updateTaskProgress('tuesday', 2, this.checked)">
                            <label class="task-label" for="tue-task-2">Complete Review Session (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('tuesday', 3)">
                            <input type="checkbox" class="task-checkbox" id="tue-task-3" onchange="updateTaskProgress('tuesday', 3, this.checked)">
                            <label class="task-label" for="tue-task-3">Maintain positive mindset</label>
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
                        <span>Wednesday</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="wednesday-icon"></i>
                </div>
                <div class="day-content" id="wednesday-content">
                    <div class="task-list">
                        <div class="task-item" onclick="toggleTask('wednesday', 0)">
                            <input type="checkbox" class="task-checkbox" id="wed-task-0" onchange="updateTaskProgress('wednesday', 0, this.checked)">
                            <label class="task-label" for="wed-task-0">Complete Deep Focus Study (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('wednesday', 1)">
                            <input type="checkbox" class="task-checkbox" id="wed-task-1" onchange="updateTaskProgress('wednesday', 1, this.checked)">
                            <label class="task-label" for="wed-task-1">Complete Intensive Study (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('wednesday', 2)">
                            <input type="checkbox" class="task-checkbox" id="wed-task-2" onchange="updateTaskProgress('wednesday', 2, this.checked)">
                            <label class="task-label" for="wed-task-2">Complete Review Session (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('wednesday', 3)">
                            <input type="checkbox" class="task-checkbox" id="wed-task-3" onchange="updateTaskProgress('wednesday', 3, this.checked)">
                            <label class="task-label" for="wed-task-3">Maintain positive mindset</label>
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
                        <span>Thursday</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="thursday-icon"></i>
                </div>
                <div class="day-content" id="thursday-content">
                    <div class="task-list">
                        <div class="task-item" onclick="toggleTask('thursday', 0)">
                            <input type="checkbox" class="task-checkbox" id="thu-task-0" onchange="updateTaskProgress('thursday', 0, this.checked)">
                            <label class="task-label" for="thu-task-0">Complete Deep Focus Study (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('thursday', 1)">
                            <input type="checkbox" class="task-checkbox" id="thu-task-1" onchange="updateTaskProgress('thursday', 1, this.checked)">
                            <label class="task-label" for="thu-task-1">Complete Intensive Study (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('thursday', 2)">
                            <input type="checkbox" class="task-checkbox" id="thu-task-2" onchange="updateTaskProgress('thursday', 2, this.checked)">
                            <label class="task-label" for="thu-task-2">Complete Review Session (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('thursday', 3)">
                            <input type="checkbox" class="task-checkbox" id="thu-task-3" onchange="updateTaskProgress('thursday', 3, this.checked)">
                            <label class="task-label" for="thu-task-3">Maintain positive mindset</label>
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
                        <span>Friday</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="friday-icon"></i>
                </div>
                <div class="day-content" id="friday-content">
                    <div class="task-list">
                        <div class="task-item" onclick="toggleTask('friday', 0)">
                            <input type="checkbox" class="task-checkbox" id="fri-task-0" onchange="updateTaskProgress('friday', 0, this.checked)">
                            <label class="task-label" for="fri-task-0">Complete Deep Focus Study (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('friday', 1)">
                            <input type="checkbox" class="task-checkbox" id="fri-task-1" onchange="updateTaskProgress('friday', 1, this.checked)">
                            <label class="task-label" for="fri-task-1">Complete Intensive Study (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('friday', 2)">
                            <input type="checkbox" class="task-checkbox" id="fri-task-2" onchange="updateTaskProgress('friday', 2, this.checked)">
                            <label class="task-label" for="fri-task-2">Complete Review Session (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('friday', 3)">
                            <input type="checkbox" class="task-checkbox" id="fri-task-3" onchange="updateTaskProgress('friday', 3, this.checked)">
                            <label class="task-label" for="fri-task-3">Maintain positive mindset</label>
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
                        <span>Saturday</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="saturday-icon"></i>
                </div>
                <div class="day-content" id="saturday-content">
                    <div class="task-list">
                        <div class="task-item" onclick="toggleTask('saturday', 0)">
                            <input type="checkbox" class="task-checkbox" id="sat-task-0" onchange="updateTaskProgress('saturday', 0, this.checked)">
                            <label class="task-label" for="sat-task-0">Complete Deep Focus Study (6:00-7:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('saturday', 1)">
                            <input type="checkbox" class="task-checkbox" id="sat-task-1" onchange="updateTaskProgress('saturday', 1, this.checked)">
                            <label class="task-label" for="sat-task-1">Complete Intensive Study (8:30-10:00 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('saturday', 2)">
                            <input type="checkbox" class="task-checkbox" id="sat-task-2" onchange="updateTaskProgress('saturday', 2, this.checked)">
                            <label class="task-label" for="sat-task-2">Complete Review Session (10:00-10:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('saturday', 3)">
                            <input type="checkbox" class="task-checkbox" id="sat-task-3" onchange="updateTaskProgress('saturday', 3, this.checked)">
                            <label class="task-label" for="sat-task-3">Maintain positive mindset</label>
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
                        <span>Sunday</span>
                    </div>
                    <i class="fas fa-chevron-down expand-icon" id="sunday-icon"></i>
                </div>
                <div class="day-content" id="sunday-content">
                    <div class="task-list">
                        <div class="task-item" onclick="toggleTask('sunday', 0)">
                            <input type="checkbox" class="task-checkbox" id="sun-task-0" onchange="updateTaskProgress('sunday', 0, this.checked)">
                            <label class="task-label" for="sun-task-0">Complete Morning Session (10:00-11:30 AM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('sunday', 1)">
                            <input type="checkbox" class="task-checkbox" id="sun-task-1" onchange="updateTaskProgress('sunday', 1, this.checked)">
                            <label class="task-label" for="sun-task-1">Complete Study Marathon (6:00-8:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('sunday', 2)">
                            <input type="checkbox" class="task-checkbox" id="sun-task-2" onchange="updateTaskProgress('sunday', 2, this.checked)">
                            <label class="task-label" for="sun-task-2">Complete Reflective Review (9:30-10:30 PM)</label>
                        </div>
                        <div class="task-item" onclick="toggleTask('sunday', 3)">
                            <input type="checkbox" class="task-checkbox" id="sun-task-3" onchange="updateTaskProgress('sunday', 3, this.checked)">
                            <label class="task-label" for="sun-task-3">Plan for upcoming week</label>
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
                "Every small step creates tomorrow's success"
                <i class="fas fa-star" style="color: #feca57;"></i>
            </div>
            <div class="footer-signature">
                Crafted with love for Mathu's excellence ✨
            </div>
        </div>
    </div>

    <div class="floating-buttons">
        <button class="floating-btn" onclick="scrollToTop()" title="Back to Top">
            <i class="fas fa-arrow-up"></i>
        </button>
        <button class="floating-btn" onclick="refreshQuote()" title="New Quote">
            <i class="fas fa-quote-right"></i>
        </button>
    </div>

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

        let touchStartY = 0;
        let touchStartTime = 0;
        let pullToRefreshActive = false;

        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            loadProgressData();
            updateAllStats();
            refreshQuote();
            setupPullToRefresh();
            setupTouchInteractions();
            
            // Load saved progress from in-memory storage
            const savedData = sessionStorage.getItem('mathuStudyTracker');
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

        // Setup pull-to-refresh functionality
        function setupPullToRefresh() {
            const pullToRefreshElement = document.getElementById('pullToRefresh');
            
            document.addEventListener('touchstart', (e) => {
                if (window.scrollY === 0) {
                    touchStartY = e.touches[0].clientY;
                    touchStartTime = Date.now();
                }
            }, { passive: true });

            document.addEventListener('touchmove', (e) => {
                if (window.scrollY === 0 && touchStartY > 0) {
                    const currentY = e.touches[0].clientY;
                    const pullDistance = currentY - touchStartY;
                    
                    if (pullDistance > 0 && pullDistance < 100) {
                        pullToRefreshElement.style.top = (pullDistance - 60) + 'px';
                        if (pullDistance > 60) {
                            pullToRefreshElement.classList.add('visible');
                            pullToRefreshActive = true;
                        }
                    }
                }
            }, { passive: true });

            document.addEventListener('touchend', () => {
                if (pullToRefreshActive) {
                    pullToRefreshElement.style.top = '-60px';
                    pullToRefreshElement.classList.remove('visible');
                    pullToRefreshActive = false;
                    
                    // Trigger refresh
                    refreshQuote();
                    updateAllStats();
                    showNotification('Data refreshed! 🔄');
                }
                touchStartY = 0;
            }, { passive: true });
        }

        // Setup touch interactions
        function setupTouchInteractions() {
            // Add haptic feedback for supported devices
            function vibrate(pattern = 10) {
                if (navigator.vibrate) {
                    navigator.vibrate(pattern);
                }
            }

            // Add touch feedback to interactive elements
            document.querySelectorAll('.task-item, .day-header, .stat-card').forEach(element => {
                element.addEventListener('touchstart', () => {
                    element.style.transform = 'scale(0.98)';
                    vibrate(5);
                }, { passive: true });

                element.addEventListener('touchend', () => {
                    setTimeout(() => {
                        element.style.transform = '';
                    }, 150);
                }, { passive: true });
            });
        }

        // Show schedule based on tab selection
        function showSchedule(type) {
            document.querySelectorAll('.schedule-tab').forEach(tab => {
                tab.classList.remove('active');
            });
            document.querySelectorAll('.schedule-content').forEach(content => {
                content.classList.remove('active');
            });

            event.target.classList.add('active');
            document.getElementById(type + '-schedule').classList.add('active');
        }

        // Toggle day section visibility with smooth animation
        function toggleDay(day) {
            const content = document.getElementById(day + '-content');
            const icon = document.getElementById(day + '-icon');
            
            if (content.classList.contains('active')) {
                content.classList.remove('active');
                icon.classList.remove('rotated');
            } else {
                // Close other open days on mobile for better UX
                if (window.innerWidth <= 768) {
                    document.querySelectorAll('.day-content.active').forEach(otherContent => {
                        if (otherContent !== content) {
                            otherContent.classList.remove('active');
                            const otherDay = otherContent.id.replace('-content', '');
                            document.getElementById(otherDay + '-icon').classList.remove('rotated');
                        }
                    });
                }
                
                content.classList.add('active');
                icon.classList.add('rotated');
                
                // Scroll to the opened section on mobile
                setTimeout(() => {
                    if (window.innerWidth <= 768) {
                        content.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                    }
                }, 300);
            }
        }

        // Toggle task with improved mobile interaction
        function toggleTask(day, taskIndex) {
            // Prevent double-tap zoom on mobile
            event.preventDefault();
            
            const checkbox = document.getElementById(getTaskId(day, taskIndex));
            if (checkbox && event.target !== checkbox) {
                checkbox.checked = !checkbox.checked;
                updateTaskProgress(day, taskIndex, checkbox.checked);
            }
        }

        // Update task progress with enhanced feedback
        function updateTaskProgress(day, taskIndex, completed) {
            dailyData[day][taskIndex] = completed;
            
            // Update visual feedback
            const label = document.querySelector(`label[for="${getTaskId(day, taskIndex)}"]`);
            if (completed) {
                label.classList.add('task-completed');
                showCelebration();
                showNotification('Task completed! 🎉');
                
                // Haptic feedback
                if (navigator.vibrate) {
                    navigator.vibrate([10, 50, 10]);
                }
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
            }).catch(error => {
                console.log('Could not sync with server');
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

        // Update progress bar with smooth animation
        function updateProgressBar(day) {
            const completedTasks = dailyData[day].filter(task => task).length;
            const totalTasks = dailyData[day].length;
            const percentage = (completedTasks / totalTasks) * 100;
            
            const progressBar = document.getElementById(day + '-progress');
            if (progressBar) {
                // Smooth animation
                progressBar.style.transition = 'width 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
                progressBar.style.width = percentage + '%';
            }
        }

        // Update all progress bars
        function updateAllProgressBars() {
            Object.keys(dailyData).forEach(day => {
                updateProgressBar(day);
            });
        }

        // Update all statistics with smooth counting animation
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
            
            // Animate counter updates
            animateCounter('total-tasks', completedTasks);
            animateCounter('completion-rate', completionRate, '%');
            animateCounter('streak-count', calculateStreak());
            animateCounter('weekly-progress', weeklyProgress, '%');
        }

        // Animate counter with smooth transition
        function animateCounter(elementId, targetValue, suffix = '') {
            const element = document.getElementById(elementId);
            const currentValue = parseInt(element.textContent) || 0;
            const increment = targetValue > currentValue ? 1 : -1;
            const duration = 1000;
            const steps = Math.abs(targetValue - currentValue);
            const stepDuration = steps > 0 ? duration / steps : 0;
            
            let current = currentValue;
            const timer = setInterval(() => {
                current += increment;
                element.textContent = current + suffix;
                
                if (current === targetValue) {
                    clearInterval(timer);
                }
            }, stepDuration);
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

        // Save progress data to session storage (no localStorage)
        function saveProgressData() {
            try {
                sessionStorage.setItem('mathuStudyTracker', JSON.stringify(dailyData));
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
