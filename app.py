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
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, maximum-scale=1.0, minimum-scale=1.0">
    <title>Mathu's Mobile Study Tracker</title>
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="theme-color" content="#667eea">
    <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiTWF0aHUncyBTdHVkeSBUcmFja2VyIiwic2hvcnRfbmFtZSI6IlN0dWR5VHJhY2tlciIsImRpc3BsYXkiOiJzdGFuZGFsb25lIiwic3RhcnRfdXJsIjoiLyIsInRoZW1lX2NvbG9yIjoiIzY2N2VlYSIsImJhY2tncm91bmRfY29sb3IiOiIjNjY3ZWVhIn0=">
    
    <!-- Preload critical resources -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdnjs.cloudflare.com">
    
    <!-- Optimized font loading -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    
    <style>
        :root {
            --primary: #667eea;
            --secondary: #764ba2;
            --accent: #f093fb;
            --success: #4facfe;
            --warning: #43e97b;
            --danger: #f5576c;
            --white: #ffffff;
            --light-gray: #f8f9fa;
            --dark-gray: #2d3748;
            --medium-gray: #4a5568;
            
            --glass-bg: rgba(255, 255, 255, 0.15);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            
            --radius: 16px;
            --radius-sm: 12px;
            --radius-lg: 20px;
            
            --space-xs: 8px;
            --space-sm: 12px;
            --space-md: 16px;
            --space-lg: 20px;
            --space-xl: 24px;
            --space-2xl: 32px;
            
            --font-xs: 0.75rem;
            --font-sm: 0.875rem;
            --font-base: 1rem;
            --font-lg: 1.125rem;
            --font-xl: 1.25rem;
            --font-2xl: 1.5rem;
            --font-3xl: 1.875rem;
            
            --touch-target: 48px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
            -webkit-touch-callout: none;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
        }

        input, textarea {
            -webkit-user-select: auto;
            -moz-user-select: auto;
            -ms-user-select: auto;
            user-select: auto;
        }

        html {
            font-size: 16px;
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            min-height: 100vh;
            min-height: 100dvh;
            overflow-x: hidden;
            font-size: var(--font-base);
            line-height: 1.5;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            position: relative;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .container {
            width: 100%;
            max-width: 100vw;
            margin: 0 auto;
            padding: var(--space-md);
            position: relative;
            z-index: 1;
        }

        /* Mobile-first header */
        .header {
            text-align: center;
            padding: var(--space-lg) 0 var(--space-xl);
            margin-bottom: var(--space-lg);
        }

        .main-title {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2rem, 8vw, 2.5rem);
            font-weight: 700;
            background: linear-gradient(45deg, var(--white), #f0f8ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 4px 20px rgba(0,0,0,0.3);
            margin-bottom: var(--space-sm);
            line-height: 1.2;
        }

        .subtitle {
            font-size: var(--font-sm);
            color: rgba(255, 255, 255, 0.9);
            font-weight: 500;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        /* Optimized glass cards */
        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: var(--radius);
            border: 1px solid var(--glass-border);
            box-shadow: var(--shadow);
            margin: var(--space-lg) 0;
            position: relative;
            overflow: hidden;
            will-change: transform;
        }

        /* Mobile-optimized quote section */
        .quote-section {
            text-align: center;
            padding: var(--space-xl);
        }

        .quote-text {
            font-size: clamp(1.125rem, 4vw, 1.25rem);
            font-style: italic;
            color: var(--white);
            margin-bottom: var(--space-md);
            line-height: 1.4;
            font-weight: 400;
        }

        .quote-author {
            font-size: var(--font-base);
            color: rgba(255, 255, 255, 0.8);
            font-weight: 500;
            margin-bottom: var(--space-xl);
        }

        .refresh-quote-btn {
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            color: var(--white);
            border: none;
            padding: var(--space-md) var(--space-xl);
            border-radius: 50px;
            font-size: var(--font-base);
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: var(--shadow);
            min-height: var(--touch-target);
            min-width: 140px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: var(--space-xs);
            margin: 0 auto;
            touch-action: manipulation;
        }

        .refresh-quote-btn:active {
            transform: scale(0.95);
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }

        /* Mobile-first stats grid */
        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--space-md);
            margin: var(--space-xl) 0;
        }

        .stat-card {
            text-align: center;
            padding: var(--space-lg);
            border-radius: var(--radius);
            position: relative;
            overflow: hidden;
            transition: transform 0.2s ease;
            min-height: 100px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            touch-action: manipulation;
        }

        .stat-card:active {
            transform: scale(0.95);
        }

        .stat-card:nth-child(1) { background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%); }
        .stat-card:nth-child(2) { background: linear-gradient(135deg, var(--accent) 0%, var(--danger) 100%); }
        .stat-card:nth-child(3) { background: linear-gradient(135deg, var(--success) 0%, #00f2fe 100%); }
        .stat-card:nth-child(4) { background: linear-gradient(135deg, var(--warning) 0%, #38f9d7 100%); }

        .stat-number {
            font-size: clamp(1.5rem, 6vw, 2rem);
            font-weight: 900;
            color: var(--white);
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
            margin-bottom: var(--space-xs);
            line-height: 1;
        }

        .stat-label {
            font-size: var(--font-xs);
            color: rgba(255, 255, 255, 0.9);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            line-height: 1.2;
        }

        /* Mobile-optimized day cards */
        .days-container {
            margin: var(--space-xl) 0;
        }

        .day-card {
            margin: var(--space-lg) 0;
            border-radius: var(--radius);
            overflow: hidden;
            transition: transform 0.2s ease;
        }

        .day-header {
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--white);
            padding: var(--space-lg);
            cursor: pointer;
            font-size: var(--font-lg);
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.2s ease;
            position: relative;
            overflow: hidden;
            min-height: var(--touch-target);
            touch-action: manipulation;
        }

        .day-header:active {
            background: linear-gradient(135deg, var(--accent) 0%, var(--danger) 100%);
            transform: scale(0.98);
        }

        .day-name {
            display: flex;
            align-items: center;
            gap: var(--space-sm);
            flex: 1;
        }

        .day-emoji {
            font-size: var(--font-xl);
        }

        .expand-icon {
            font-size: var(--font-lg);
            transition: transform 0.3s ease;
            padding: var(--space-xs);
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
            max-height: 800px;
        }

        .task-list {
            padding: var(--space-lg);
        }

        /* Mobile-optimized task items */
        .task-item {
            display: flex;
            align-items: center;
            padding: var(--space-lg);
            margin: var(--space-sm) 0;
            background: rgba(255, 255, 255, 0.9);
            border-radius: var(--radius-sm);
            border-left: 4px solid #4299e1;
            transition: all 0.2s ease;
            cursor: pointer;
            position: relative;
            min-height: var(--touch-target);
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            touch-action: manipulation;
        }

        .task-item:active {
            transform: scale(0.98);
            background: rgba(255, 255, 255, 1);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }

        .task-checkbox {
            width: 20px;
            height: 20px;
            margin-right: var(--space-md);
            cursor: pointer;
            accent-color: #4299e1;
            transform: scale(1.2);
            flex-shrink: 0;
            touch-action: manipulation;
        }

        .task-label {
            font-size: var(--font-base);
            color: var(--dark-gray);
            cursor: pointer;
            flex: 1;
            font-weight: 500;
            transition: all 0.2s ease;
            line-height: 1.4;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
        }

        .task-completed {
            text-decoration: line-through;
            color: var(--medium-gray);
            opacity: 0.7;
        }

        .progress-bar {
            width: 100%;
            height: 6px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 3px;
            margin-top: var(--space-md);
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(135deg, var(--success) 0%, #00f2fe 100%);
            border-radius: 3px;
            transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
        }

        /* Mobile schedule section */
        .schedule-section {
            padding: var(--space-xl);
        }

        .schedule-header {
            font-family: 'Playfair Display', serif;
            font-size: clamp(1.5rem, 5vw, 1.875rem);
            font-weight: 600;
            text-align: center;
            margin-bottom: var(--space-xl);
            color: var(--white);
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }

        .schedule-tabs {
            display: flex;
            background: rgba(255, 255, 255, 0.2);
            border-radius: var(--radius);
            margin-bottom: var(--space-xl);
            overflow: hidden;
        }

        .schedule-tab {
            flex: 1;
            padding: var(--space-md);
            background: transparent;
            border: none;
            color: var(--white);
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            min-height: var(--touch-target);
            font-size: var(--font-base);
            touch-action: manipulation;
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
            padding: var(--space-lg);
            margin: var(--space-sm) 0;
            background: rgba(255, 255, 255, 0.9);
            border-radius: var(--radius-sm);
            border-left: 6px solid;
            transition: all 0.2s ease;
            position: relative;
            overflow: hidden;
            min-height: 60px;
            touch-action: manipulation;
        }

        .schedule-item:active {
            transform: scale(0.98);
        }

        .study-session { border-color: #e53e3e; }
        .dinner { border-color: #38b2ac; }
        .revision { border-color: #3182ce; }
        .morning { border-color: #d69e2e; }
        .evening { border-color: #9f7aea; }
        .night { border-color: #4299e1; }

        .time-slot {
            font-weight: 700;
            font-size: var(--font-sm);
            color: var(--dark-gray);
            min-width: 100px;
            padding: var(--space-xs) var(--space-sm);
            background: linear-gradient(45deg, #f7fafc, #edf2f7);
            border-radius: var(--space-xs);
            border: 1px solid #e2e8f0;
            text-align: center;
            flex-shrink: 0;
        }

        .activity-name {
            font-size: var(--font-base);
            color: var(--medium-gray);
            margin-left: var(--space-md);
            font-weight: 500;
            flex: 1;
            line-height: 1.3;
        }

        .activity-icon {
            font-size: var(--font-xl);
            margin-right: var(--space-sm);
            flex-shrink: 0;
        }

        /* Mobile footer */
        .footer {
            text-align: center;
            margin-top: var(--space-2xl);
            padding: var(--space-2xl);
            border-radius: var(--radius);
        }

        .footer-message {
            font-size: var(--font-lg);
            color: var(--white);
            font-weight: 500;
            margin-bottom: var(--space-sm);
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }

        .footer-signature {
            font-size: var(--font-base);
            color: rgba(255, 255, 255, 0.8);
            font-style: italic;
        }

        /* Mobile floating buttons */
        .floating-buttons {
            position: fixed;
            bottom: var(--space-lg);
            right: var(--space-lg);
            display: flex;
            flex-direction: column;
            gap: var(--space-sm);
            z-index: 1000;
        }

        .floating-btn {
            width: 56px;
            height: 56px;
            border-radius: 50%;
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            border: none;
            color: var(--white);
            font-size: var(--font-lg);
            cursor: pointer;
            box-shadow: 0 4px 16px rgba(0,0,0,0.3);
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            touch-action: manipulation;
        }

        .floating-btn:active {
            transform: scale(0.9);
        }

        /* Loading spinner */
        .loading {
            display: inline-block;
            width: 16px;
            height: 16px;
            border: 2px solid rgba(255,255,255,.3);
            border-radius: 50%;
            border-top-color: var(--white);
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Celebration animation */
        .celebration {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 3rem;
            z-index: 2000;
            pointer-events: none;
            animation: celebrate 2s ease-out forwards;
        }

        @keyframes celebrate {
            0% { opacity: 0; transform: translate(-50%, -50%) scale(0); }
            50% { opacity: 1; transform: translate(-50%, -50%) scale(1.2); }
            100% { opacity: 0; transform: translate(-50%, -50%) scale(1); }
        }

        /* Toast notification */
        .toast {
            position: fixed;
            bottom: 100px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.8);
            color: var(--white);
            padding: var(--space-md) var(--space-lg);
            border-radius: var(--radius);
            font-size: var(--font-sm);
            font-weight: 500;
            z-index: 2000;
            opacity: 0;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .toast.show {
            opacity: 1;
            transform: translateX(-50%) translateY(-10px);
        }

        /* Small mobile devices */
        @media (max-width: 375px) {
            .container { padding: var(--space-sm); }
            .main-title { font-size: 1.75rem; }
            .quote-text { font-size: 1rem; }
            .stat-number { font-size: 1.5rem; }
            .day-header { padding: var(--space-md); font-size: var(--font-base); }
            .task-item { padding: var(--space-md); }
            .time-slot { min-width: 90px; font-size: var(--font-xs); }
            .floating-btn { width: 48px; height: 48px; }
        }

        /* Large mobile devices */
        @media (min-width: 414px) {
            .stats-grid { gap: var(--space-lg); }
            .stat-card { min-height: 120px; }
        }

        /* Landscape orientation */
        @media (orientation: landscape) and (max-height: 600px) {
            .header { padding: var(--space-md) 0; margin-bottom: var(--space-md); }
            .main-title { font-size: 1.75rem; margin-bottom: var(--space-xs); }
            .subtitle { font-size: var(--font-xs); }
            .stats-grid { grid-template-columns: repeat(4, 1fr); }
            .stat-card { padding: var(--space-md); min-height: 80px; }
        }

        /* Dark mode support */
        @media (prefers-color-scheme: dark) {
            .glass-card { background: rgba(0, 0, 0, 0.3); border: 1px solid rgba(255, 255, 255, 0.1); }
            .day-content { background: rgba(0, 0, 0, 0.7); }
            .task-item { background: rgba(255, 255, 255, 0.1); }
            .task-label { color: var(--white); }
            .schedule-item { background: rgba(255, 255, 255, 0.1); }
            .time-slot { background: rgba(255, 255, 255, 0.2); color: var(--white); border-color: rgba(255, 255, 255, 0.1); }
            .activity-name { color: rgba(255, 255, 255, 0.9); }
        }

        /* Reduced motion */
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }

        /* High contrast */
        @media (prefers-contrast: high) {
            .glass-card { background: rgba(255, 255, 255, 0.9); border: 2px solid #000; }
            .task-item { border: 2px solid #000; }
        }

        /* Focus indicators */
        button:focus-visible, input:focus-visible, .task-item:focus-visible {
            outline: 2px solid var(--success);
            outline-offset: 2px;
        }

        /* Performance optimizations */
        .day-card, .stat-card, .task-item, .schedule-item {
            will-change: transform;
        }

        /* iOS safe area support */
        @supports (padding: max(0px)) {
            .container {
                padding-left: max(var(--space-md), env(safe-area-inset-left));
                padding-right: max(var(--space-md), env(safe-area-inset-right));
                padding-bottom: max(var(--space-md), env(safe-area-inset-bottom));
            }
            
            .floating-buttons {
                bottom: max(var(--space-lg), env(safe-area-inset-bottom));
                right: max(var(--space-lg), env(safe-area-inset-right));
            }
        }
    </style>
</head>
<body>
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

        <div class="stats-grid">
            <div class="stat-card">
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

        // Mobile-optimized variables
        let isScrolling = false;
        let lastScrollTop = 0;
        let vibrationSupported = 'vibrate' in navigator;

        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            initializeMobileApp();
            loadProgressData();
            updateAllStats();
            refreshQuote();
            setupMobileInteractions();
            
            // Load saved progress from sessionStorage (mobile-safe)
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

        // Initialize mobile-specific features
        function initializeMobileApp() {
            // Prevent zoom on double tap
            let lastTouchEnd = 0;
            document.addEventListener('touchend', function (event) {
                const now = (new Date()).getTime();
                if (now - lastTouchEnd <= 300) {
                    event.preventDefault();
                }
                lastTouchEnd = now;
            }, false);

            // Handle viewport changes
            window.addEventListener('resize', debounce(handleViewportChange, 250));
            window.addEventListener('orientationchange', handleOrientationChange);

            // Prevent overscroll bounce on iOS
            document.body.addEventListener('touchstart', handleTouchStart, { passive: false });
            document.body.addEventListener('touchmove', handleTouchMove, { passive: false });

            // Add app-like behavior
            if (window.matchMedia('(display-mode: standalone)').matches) {
                document.body.classList.add('standalone-app');
            }
        }

        // Setup mobile interactions
        function setupMobileInteractions() {
            // Add touch feedback to all interactive elements
            const interactiveElements = document.querySelectorAll(
                '.task-item, .day-header, .stat-card, .schedule-item, .refresh-quote-btn, .schedule-tab, .floating-btn'
            );

            interactiveElements.forEach(element => {
                element.addEventListener('touchstart', handleTouchFeedback, { passive: true });
                element.addEventListener('touchend', removeTouchFeedback, { passive: true });
                element.addEventListener('touchcancel', removeTouchFeedback, { passive: true });
            });

            // Setup swipe gestures
            setupSwipeGestures();
            
            // Setup pull-to-refresh
            setupPullToRefresh();
        }

        // Handle touch feedback
        function handleTouchFeedback(e) {
            const element = e.currentTarget;
            element.style.transform = 'scale(0.95)';
            element.style.transition = 'transform 0.1s ease';
            
            // Haptic feedback
            if (vibrationSupported) {
                navigator.vibrate(10);
            }
        }

        // Remove touch feedback
        function removeTouchFeedback(e) {
            const element = e.currentTarget;
            setTimeout(() => {
                element.style.transform = '';
                element.style.transition = 'transform 0.2s ease';
            }, 100);
        }

        // Setup swipe gestures
        function setupSwipeGestures() {
            let touchStartX = 0;
            let touchStartY = 0;
            let touchEndX = 0;
            let touchEndY = 0;

            document.addEventListener('touchstart', (e) => {
                touchStartX = e.changedTouches[0].screenX;
                touchStartY = e.changedTouches[0].screenY;
            }, { passive: true });

            document.addEventListener('touchend', (e) => {
                touchEndX = e.changedTouches[0].screenX;
                touchEndY = e.changedTouches[0].screenY;
                handleSwipe();
            }, { passive: true });

            function handleSwipe() {
                const swipeThreshold = 50;
                const diffX = touchStartX - touchEndX;
                const diffY = touchStartY - touchEndY;

                if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > swipeThreshold) {
                    if (diffX > 0) {
                        // Swipe left - could close expanded sections
                        closeAllExpandedSections();
                    }
                }
            }
        }

        // Setup pull-to-refresh
        function setupPullToRefresh() {
            let pullStartY = 0;
            let pullCurrentY = 0;
            let pulling = false;
            const pullThreshold = 80;

            document.addEventListener('touchstart', (e) => {
                if (window.scrollY === 0) {
                    pullStartY = e.touches[0].clientY;
                }
            }, { passive: true });

            document.addEventListener('touchmove', (e) => {
                if (window.scrollY === 0 && pullStartY > 0) {
                    pullCurrentY = e.touches[0].clientY;
                    const pullDistance = pullCurrentY - pullStartY;
                    
                    if (pullDistance > 0 && pullDistance < pullThreshold * 2) {
                        pulling = pullDistance > pullThreshold;
                        // Visual feedback could be added here
                    }
                }
            }, { passive: true });

            document.addEventListener('touchend', () => {
                if (pulling) {
                    refreshData();
                    showToast('Refreshing data...', 2000);
                }
                pullStartY = 0;
                pullCurrentY = 0;
                pulling = false;
            }, { passive: true });
        }

        // Handle viewport changes
        function handleViewportChange() {
            // Adjust layout based on new viewport
            const vh = window.innerHeight * 0.01;
            document.documentElement.style.setProperty('--vh', `${vh}px`);
        }

        // Handle orientation change
        function handleOrientationChange() {
            setTimeout(() => {
                handleViewportChange();
                // Close expanded sections in landscape for better UX
                if (window.innerHeight < window.innerWidth) {
                    closeAllExpandedSections();
                }
            }, 100);
        }

        // Prevent overscroll
        function handleTouchStart(e) {
            if (e.touches.length === 1) {
                // Allow normal scrolling
            }
        }

        function handleTouchMove(e) {
            const touch = e.touches[0];
            const element = e.target;
            
            // Prevent overscroll at top and bottom
            if (window.scrollY === 0 && touch.clientY > lastTouchTop) {
                // At top, trying to scroll up
                if (!element.closest('.day-content')) {
                    e.preventDefault();
                }
            }
            
            lastTouchTop = touch.clientY;
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
            
            // Haptic feedback
            if (vibrationSupported) {
                navigator.vibrate(15);
            }
        }

        // Toggle day section with mobile optimizations
        function toggleDay(day) {
            const content = document.getElementById(day + '-content');
            const icon = document.getElementById(day + '-icon');
            const wasActive = content.classList.contains('active');
            
            // Close all other sections on mobile
            closeAllExpandedSections();
            
            if (!wasActive) {
                content.classList.add('active');
                icon.classList.add('rotated');
                
                // Smooth scroll to section
                setTimeout(() => {
                    const header = document.querySelector(`#${day}-content`).previousElementSibling;
                    header.scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'start',
                        inline: 'nearest'
                    });
                }, 300);
                
                // Haptic feedback
                if (vibrationSupported) {
                    navigator.vibrate(20);
                }
            }
        }

        // Close all expanded sections
        function closeAllExpandedSections() {
            document.querySelectorAll('.day-content.active').forEach(content => {
                content.classList.remove('active');
            });
            document.querySelectorAll('.expand-icon.rotated').forEach(icon => {
                icon.classList.remove('rotated');
            });
        }

        // Toggle task with mobile optimizations
        function toggleTask(day, taskIndex) {
            event.preventDefault();
            event.stopPropagation();
            
            const checkbox = document.getElementById(getTaskId(day, taskIndex));
            if (checkbox && event.target !== checkbox) {
                checkbox.checked = !checkbox.checked;
                updateTaskProgress(day, taskIndex, checkbox.checked);
            }
        }

        // Update task progress with enhanced mobile feedback
        function updateTaskProgress(day, taskIndex, completed) {
            dailyData[day][taskIndex] = completed;
            
            // Update visual feedback
            const label = document.querySelector(`label[for="${getTaskId(day, taskIndex)}"]`);
            if (completed) {
                label.classList.add('task-completed');
                showCelebration();
                showToast('Task completed! 🎉', 2000);
                
                // Enhanced haptic feedback
                if (vibrationSupported) {
                    navigator.vibrate([10, 50, 10]);
                }
            } else {
                label.classList.remove('task-completed');
                showToast('Task unchecked', 1000);
            }
            
            // Update progress bar
            updateProgressBar(day);
            
            // Update statistics
            updateAllStats();
            
            // Save progress
            saveProgressData();
            
            // Sync with backend
            syncWithBackend(day, taskIndex, completed);
        }

        // Get task ID helper
        function getTaskId(day, taskIndex) {
            const dayPrefixes = {
                monday: 'mon', tuesday: 'tue', wednesday: 'wed', thursday: 'thu',
                friday: 'fri', saturday: 'sat', sunday: 'sun'
            };
            return `${dayPrefixes[day]}-task-${taskIndex}`;
        }

        // Update progress bar with smooth mobile animation
        function updateProgressBar(day) {
            const completedTasks = dailyData[day].filter(task => task).length;
            const totalTasks = dailyData[day].length;
            const percentage = (completedTasks / totalTasks) * 100;
            
            const progressBar = document.getElementById(day + '-progress');
            if (progressBar) {
                progressBar.style.transition = 'width 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
                progressBar.style.width = percentage + '%';
            }
        }

        // Update all progress bars
        function updateAllProgressBars() {
            Object.keys(dailyData).forEach(day => {
                updateProgressBar(day);
            });
        }

        // Update all statistics with mobile-optimized animations
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
            
            // Animate counters with mobile-friendly timing
            animateCounter('total-tasks', completedTasks);
            animateCounter('completion-rate', completionRate, '%');
            animateCounter('streak-count', calculateStreak());
            animateCounter('weekly-progress', weeklyProgress, '%');
        }

        // Mobile-optimized counter animation
        function animateCounter(elementId, targetValue, suffix = '') {
            const element = document.getElementById(elementId);
            const currentValue = parseInt(element.textContent) || 0;
            
            if (currentValue === targetValue) return;
            
            const increment = targetValue > currentValue ? 1 : -1;
            const duration = 800; // Shorter for mobile
            const steps = Math.abs(targetValue - currentValue);
            const stepDuration = steps > 0 ? duration / steps : 0;
            
            let current = currentValue;
            const timer = setInterval(() => {
                current += increment;
                element.textContent = current + suffix;
                
                if (current === targetValue) {
                    clearInterval(timer);
                }
            }, Math.max(stepDuration, 20)); // Minimum 20ms for smooth animation
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
                    
                    if (checkbox && label) {
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

        // Mobile-safe data persistence
        function saveProgressData() {
            try {
                sessionStorage.setItem('mathuStudyTracker', JSON.stringify(dailyData));
                sessionStorage.setItem('mathuStudyTrackerTimestamp', Date.now().toString());
            } catch (e) {
                console.log('Could not save progress data');
                showToast('Save failed - storage full', 2000);
            }
        }

        // Load progress data
        function loadProgressData() {
            try {
                const saved = sessionStorage.getItem('mathuStudyTracker');
                const timestamp = sessionStorage.getItem('mathuStudyTrackerTimestamp');
                
                if (saved && timestamp) {
                    const hoursSinceLastSave = (Date.now() - parseInt(timestamp)) / (1000 * 60 * 60);
                    if (hoursSinceLastSave < 24) { // Data valid for 24 hours
                        dailyData = JSON.parse(saved);
                    }
                }
            } catch (e) {
                console.log('Could not load progress data');
            }
        }

        // Refresh motivational quote with mobile optimizations
        async function refreshQuote() {
            const button = document.querySelector('.refresh-quote-btn');
            const originalHTML = button.innerHTML;
            button.innerHTML = '<div class="loading"></div> Loading...';
            button.disabled = true;
            
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), 5000); // 5s timeout
                
                const response = await fetch('/api/quote', {
                    signal: controller.signal
                });
                clearTimeout(timeoutId);
                
                if (!response.ok) throw new Error('Network error');
                
                const data = await response.json();
                
                // Smooth transition
                const quoteElement = document.getElementById('quote-text');
                const authorElement = document.getElementById('quote-author');
                
                quoteElement.style.opacity = '0';
                authorElement.style.opacity = '0';
                
                setTimeout(() => {
                    quoteElement.textContent = `"${data.quote}"`;
                    authorElement.textContent = `- ${data.author}`;
                    quoteElement.style.opacity = '1';
                    authorElement.style.opacity = '1';
                }, 200);
                
                // Haptic feedback
                if (vibrationSupported) {
                    navigator.vibrate(25);
                }
                
                showToast('New inspiration loaded! ✨', 2000);
                
            } catch (error) {
                console.error('Error fetching quote:', error);
                showToast('Could not load new quote', 2000);
            } finally {
                button.innerHTML = originalHTML;
                button.disabled = false;
            }
        }

        // Sync with backend
        async function syncWithBackend(day, taskIndex, completed) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), 3000);
                
                await fetch('/api/progress', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ day, task_index: taskIndex, completed }),
                    signal: controller.signal
                });
                
                clearTimeout(timeoutId);
            } catch (error) {
                console.log('Could not sync with server');
                // Data is still saved locally
            }
        }

        // Refresh all data
        function refreshData() {
            updateAllStats();
            updateAllProgressBars();
            refreshQuote();
        }

        // Show celebration animation
        function showCelebration() {
            const celebrations = ['🎉✨', '🌟🎊', '🏆⭐', '🎯🔥', '💪✨'];
            const randomCelebration = celebrations[Math.floor(Math.random() * celebrations.length)];
            
            const celebration = document.createElement('div');
            celebration.className = 'celebration';
            celebration.textContent = randomCelebration;
            document.body.appendChild(celebration);
            
            setTimeout(() => {
                if (document.body.contains(celebration)) {
                    document.body.removeChild(celebration);
                }
            }, 2000);
        }

        // Mobile-optimized toast notifications
        function showToast(message, duration = 3000) {
            // Remove existing toast
            const existingToast = document.querySelector('.toast');
            if (existingToast) {
                existingToast.remove();
            }
            
            const toast = document.createElement('div');
            toast.className = 'toast';
            toast.textContent = message;
            document.body.appendChild(toast);
            
            // Show toast
            requestAnimationFrame(() => {
                toast.classList.add('show');
            });
            
            // Hide toast
            setTimeout(() => {
                toast.classList.remove('show');
                setTimeout(() => {
                    if (document.body.contains(toast)) {
                        document.body.removeChild(toast);
                    }
                }, 300);
            }, duration);
        }

        // Smooth scroll to top
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            
            if (vibrationSupported) {
                navigator.vibrate(15);
            }
        }

        // Debounce utility for mobile performance
        function debounce(func, wait) {
            let timeout;
            return function executedFunction(...args) {
                const later = () => {
                    clearTimeout(timeout);
                    func(...args);
                };
                clearTimeout(timeout);
                timeout = setTimeout(later, wait);
            };
        }

        // Throttle utility for scroll events
        function throttle(func, limit) {
            let inThrottle;
            return function() {
                const args = arguments;
                const context = this;
                if (!inThrottle) {
                    func.apply(context, args);
                    inThrottle = true;
                    setTimeout(() => inThrottle = false, limit);
                }
            }
        }

        // Handle scroll events for floating button visibility
        const handleScroll = throttle(() => {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            const floatingButtons = document.querySelector('.floating-buttons');
            
            if (scrollTop > 300) {
                floatingButtons.style.opacity = '1';
                floatingButtons.style.pointerEvents = 'auto';
            } else {
                floatingButtons.style.opacity = '0.7';
            }
            
            isScrolling = true;
            setTimeout(() => {
                isScrolling = false;
            }, 100);
        }, 16);

        window.addEventListener('scroll', handleScroll, { passive: true });

        // Handle keyboard shortcuts (for desktop testing)
        document.addEventListener('keydown', function(e) {
            if (e.ctrlKey || e.metaKey) {
                switch(e.key) {
                    case 'r':
                        e.preventDefault();
                        refreshQuote();
                        break;
                }
            }
            
            if (e.key === 'Escape') {
                closeAllExpandedSections();
            }
        });

        // Auto-save with mobile-friendly intervals
        setInterval(saveProgressData, 30000); // Save every 30 seconds

        // Handle page visibility changes (mobile app lifecycle)
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                // App going to background - save data
                saveProgressData();
            } else {
                // App coming to foreground - refresh if needed
                const lastSave = sessionStorage.getItem('mathuStudyTrackerTimestamp');
                if (lastSave) {
                    const minutesSinceLastSave = (Date.now() - parseInt(lastSave)) / (1000 * 60);
                    if (minutesSinceLastSave > 30) {
                        refreshData();
                    }
                }
                updateAllStats();
            }
        });

        // Handle network status changes
        window.addEventListener('online', () => {
            showToast('Back online! 📶', 2000);
            // Could sync pending changes here
        });

        window.addEventListener('offline', () => {
            showToast('Offline mode - data saved locally 📱', 3000);
        });

        // Initialize performance observer for mobile optimization
        if ('PerformanceObserver' in window) {
            const observer = new PerformanceObserver((list) => {
                for (const entry of list.getEntries()) {
                    if (entry.entryType === 'measure' && entry.duration > 16) {
                        console.log(`Slow operation: ${entry.name} took ${entry.duration}ms`);
                    }
                }
            });
            observer.observe({ entryTypes: ['measure'] });
        }

        // Service Worker registration for PWA features (if needed)
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                // Service worker could be registered here for offline functionality
                console.log('PWA features available');
            });
        }

        // Final mobile optimization - prevent context menu on long press
        document.addEventListener('contextmenu', function(e) {
            if (e.target.closest('.task-item, .day-header, .stat-card')) {
                e.preventDefault();
            }
        });

        // Initialize touch support check
        const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
        if (isTouchDevice) {
            document.body.classList.add('touch-device');
        }

        console.log('Mobile Study Tracker initialized successfully! 📱✨');
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
