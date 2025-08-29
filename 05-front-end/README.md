# AI-Assisted Web App Enhancement Workshop: Weather Data Dashboard

## Workshop Overview
This workshop demonstrates how GitHub Copilot can accelerate web development and prototyping. Using a weather data dashboard as our example, we'll explore how AI coding assistants can help with everything from simple CSS reorganization to building modern, interactive features.

## Learning Objectives
- Master GitHub Copilot's core features (Ask, Edit, Agent, and tool calling)
- Develop effective prompting strategies for AI-assisted coding
- Learn to manage context and file selection for optimal results
- Build confidence in using AI tools for rapid prototyping
- Understand when and how to iterate on AI suggestions

## Prerequisites
**Important**: Before attending this workshop, please ensure you have cloned the following repository:
```bash
git clone https://github.com/timmanik/data-pipeline-workshop.git
```

This repository contains the Flask application we'll be working with during the workshop.

## The Scenario
We're working with a functional Flask-based weather data dashboard that needs modernization:
- A working Flask application displaying NOAA weather data
- Mixed concerns (CSS embedded in HTML)
- Basic functionality that could benefit from enhanced user experience
- Opportunities for both simple improvements and advanced features

## Project Structure
```
flask-app/
├── app.py                 # Flask app main entry
├── docker-compose.yml     # Docker Compose config
├── Dockerfile             # Docker build config
├── requirements.txt       # Python dependencies
├── static
│   └── styles.css         # CSS styles
└── templates
    ├── index.html         # Main HTML template
    └── layout.html        # Base HTML template
```

## Workshop Flow

### Part 1: Understanding Copilot Chat Modes

GitHub Copilot Chat offers three distinct modes, each designed for different development scenarios:

#### Ask Mode - Your Instant Code Assistant
**When to use**: Quick clarifications, code explanations, or learning without modifying files

**Key features**:
- No code changes are made
- Immediate context-aware help
- Perfect for understanding existing code


#### Edit Mode - Surgical Code Updates
**When to use**: Specific, controlled changes to defined files

**Key features**:
- You choose which files can be modified
- Shows diffs before applying changes
- Full control over each edit


#### Agent Mode - Autonomous Development Partner
**When to use**: Complex, multi-step tasks requiring iteration

**Key features**:
- Autonomously determines files to modify
- Runs terminal commands (with approval)
- Iterates until task completion
- Self-corrects errors


**Agent Mode Tips**:
- Use custom instructions to define coding standards
- Be specific about requirements
- Review the autonomous changes carefully
- Use the undo feature if needed

### Part 2: Enhanced Features

#### Screenshot Integration
Copilot Chat supports image attachments for visual context:

**Use cases**:
1. **Design feedback**: Take a screenshot of your current UI, attach it, and ask: "Make this header more modern with a gradient background"
2. **Bug reports**: Screenshot an error and ask: "Why is this visualization not rendering correctly?"
3. **Mockup implementation**: Attach a design mockup and request: "Generate the HTML and CSS to match this design"

#### Model Selection
GitHub Copilot offers multiple AI models with different strengths:

**Available Models**:
- **Standard Models** (Included - no premium requests):
  - GPT-4.1 - Fast, general-purpose
  - GPT-4o - Optimized for code
  - GPT-5 mini (Preview) - Lightweight tasks

- **Premium Models** (Consume premium requests):
  - Claude Sonnet 3.5 (1x multiplier)
  - Claude Sonnet 3.7 (1x multiplier)  
  - Claude Sonnet 4 (1x multiplier) - **Recommended for complex tasks**
  - Gemini 2.5 Pro (1x multiplier)
  - GPT-5 (Preview) (1x multiplier)
  - o4-mini (Preview) (0.33x multiplier)

**Model Selection Tips**:
- Use standard models for routine coding tasks
- Switch to Claude 4 for complex refactoring or architectural decisions
- Experiment to find which model works best for your coding style

### Part 3: Basic Improvements - Learning the Fundamentals

#### 1. CSS Organization (Beginner)
**Goal**: Extract embedded CSS from `index.html` to `styles.css`

**Learning Points**:
- Using Copilot Chat's "Edit" mode
- Understanding file context selection
- Basic refactoring with AI assistance

**Exercise**:
1. Open both `index.html` and `styles.css` in your editor
2. Switch to Edit mode in Copilot Chat
3. Add both files to the context
4. Prompt: "Move all CSS from the style tag in index.html to styles.css while maintaining the same visual appearance"

#### 2. Theme Customization (Beginner)
**Goal**: Update fonts and color scheme

**Exercise Ideas**:
- Change to a modern font stack
- Update color palette to match university branding
- Adjust spacing and typography

**Prompting Strategy**:
```
"Update the color scheme to use [specific colors] for headers and 
[specific colors] for backgrounds. Change the font to [font name] 
and ensure good contrast for accessibility."
```

#### 3. Performance Optimization (Intermediate)
**Goal**: Cache the temperature distribution plot

**Using Agent Mode**:
1. Switch to Agent mode
2. Prompt: "Implement caching for the temperature distribution plot. Save it as a static image that regenerates every hour."
3. Watch as Copilot:
   - Analyzes the current implementation
   - Creates necessary directories
   - Implements caching logic
   - Adds cache invalidation

### Part 5: Intermediate Features - Building User Experience

#### 4. Dark Mode Implementation (Intermediate)
**Goal**: Add a toggle-able dark mode

**Progressive Approach with Edit Mode**:
1. Start: "Add a dark mode toggle button to the header"
2. Enhance: "Save the user's dark mode preference in localStorage"
3. Polish: "Add smooth transitions between light and dark modes"

**Screenshot Enhancement**:
- Take a screenshot after implementing basic dark mode
- Attach it and ask: "The dark mode looks too harsh. Make the colors more subtle with better contrast"

#### 5. Temperature Unit Converter (Intermediate)
**Goal**: Toggle between Celsius and Fahrenheit

**Demonstrating Prompting Excellence**:

**Basic Prompt**: 
"Add temperature converter"

**Better Prompt**: 
"Add a toggle button that converts all temperature displays between Celsius and Fahrenheit. Update the chart, statistics, and table data."

**Best Prompt with Context Questions**:
"I want to add a temperature unit converter to my weather dashboard. Before implementing, please ask me 3 questions about the specific requirements and user experience I'm looking for."

### Part 6: Advanced Features - Modern Web Development

#### 6. Multi-Page Navigation (Advanced)
**Goal**: Create a tabbed interface with multiple views

**Using Agent Mode**:
```
"Create a multi-page Flask application with:
- A navigation menu with Home, Statistics, Historical Trends, and About pages
- Use Flask blueprints for better organization
- Maintain consistent styling across all pages
- Add active page highlighting in the navigation"
```

#### 7. Modern UI Overhaul (Advanced)
**Goal**: Transform the dashboard into a contemporary web application

**Demonstrating Detailed Prompting**:

**Vague Prompt** (Don't do this):
"Make the site modern"

**Detailed Prompt** (Do this):
"Redesign the weather dashboard with a modern aesthetic:
- Use a card-based layout with subtle shadows (box-shadow: 0 2px 4px rgba(0,0,0,0.1))
- Implement a sticky navigation header with backdrop-filter blur
- Add hover animations (transform: translateY(-2px) on hover)
- Use a gradient color palette (#1a1a2e to #16213e)
- Ensure mobile responsiveness with CSS Grid
- Include skeleton loaders for data fetching states
- Add micro-interactions for all buttons and links"

## Prompting Best Practices

Based on prompt engineering principles ([source](https://www.promptingguide.ai/introduction/elements)), effective prompts contain key elements that guide AI responses:

### 1. Core Prompt Elements
- **Instruction**: Clear directive of what you want Copilot to do
- **Context**: Relevant background information about your project
- **Input Data**: Specific code, files, or examples to work with
- **Output Indicator**: Expected format or structure of the response

**Example applying all elements**:
```
[Instruction] Refactor this authentication function to use JWT tokens
[Context] This is part of a Flask app with 1000+ daily users
[Input Data] Current function uses session-based auth in app.py lines 45-67
[Output Indicator] Provide the updated function with error handling and comments
```

### 2. Advanced Prompting Techniques ([source](https://www.promptingguide.ai/introduction/tips))

**Be Specific and Detailed**
- ❌ "Fix the bug"
- ✅ "Fix the TypeError on line 23 when user_data is None by adding proper null checking"

**Use Examples (Few-shot prompting)**
```
"Convert this function to use async/await pattern like this example:
# Sync version
def get_data(): return requests.get(url)
# Async version
async def get_data(): return await aiohttp.get(url)

Now convert my fetch_weather() function similarly"
```

**Structure Complex Tasks**
Break down large requests into steps:
```
"Help me implement user authentication:
1. First, create a User model with email and hashed password
2. Then, add registration endpoint with validation
3. Finally, implement JWT token generation on login"
```

**Specify Constraints**
```
"Add error logging to all API endpoints, but:
- Use Python's built-in logging module only
- Keep log files under 10MB
- Include timestamp, endpoint, and user ID"
```

### 3. Iteration Strategies
- Start simple, then refine: "Add a navbar" → "Make it sticky" → "Add mobile menu"
- Request alternatives: "Show me 2 different ways to implement this"
- Ask for explanations: "Explain why you chose this approach"

## Context Management Strategies

Effective context management is crucial for accurate AI responses ([source](https://www.promptingguide.ai/guides/context-engineering-guide)):

### 1. Context Window Optimization
**Include What Matters**:
- Primary file being modified
- Related dependencies (imports, utilities)
- Configuration files when relevant
- Test files for TDD approaches

**Exclude Noise**:
- Unrelated modules
- Large data files
- Generated or minified code
- Cached or temporary files

### 2. Context Engineering Techniques

**Explicit File References**
```
"In templates/index.html, update the header section to match 
the new design in static/mockup.png, using styles from static/styles.css"
```

**Hierarchical Context**
Start broad, then narrow:
```
"We're building a weather dashboard with Flask.
The app.py handles API calls to NOAA.
Focus on the get_weather_data() function that needs caching."
```

**Dynamic Context Loading**
For complex features:
1. Start with core files
2. Add dependencies as needed
3. Remove files once changes are complete
4. Keep context focused on current task


### 3. Context Best Practices
- **New chat for new features**: Prevents context pollution
- **Reference specific sections**: "In the handleSubmit function..." 
- **State assumptions clearly**: "Assuming we're using Bootstrap 5..."
- **Update context progressively**: Add files as the conversation evolves

## Advanced Tips

### Premium Requests and Billing
Each time you send a prompt in a chat window or trigger a response from Copilot, you're making a request. Some Copilot features use more advanced processing power and count as premium requests.

**Managing Premium Requests** ([billing documentation](https://docs.github.com/en/copilot/concepts/billing/copilot-requests)):
- Premium requests reset monthly (1st of month at 00:00 UTC)
- Many accounts have a default $0 budget limit, meaning once you use all included premium requests, additional requests are rejected (not billed)
- To use more premium requests, adjust or remove the spending limit in settings
- Monitor usage via VS Code status bar or GitHub settings

### Response Customization
While out of scope for this workshop, be aware that GitHub Copilot supports:
- Custom instructions per repository
- Team-specific coding standards
- Automated response patterns

Learn more: https://docs.github.com/en/copilot/concepts/response-customization

## Common Pitfalls and Solutions

### Pitfall 1: Accepting First Suggestion
**Solution**: Always iterate! Ask for improvements or alternatives

### Pitfall 2: Losing Context
**Solution**: Manage open files carefully, use explicit file references

### Pitfall 3: Vague Prompts
**Solution**: Include specific requirements, visual descriptions, and examples

### Pitfall 4: Ignoring Premium Request Usage
**Solution**: Monitor usage regularly, use standard models when appropriate

### Pitfall 5: Not Using Visual Context
**Solution**: Leverage screenshots for UI improvements

## Resources and References

### Official Documentation
- **Prompt Engineering Guide**: https://docs.github.com/en/copilot/concepts/prompt-engineering
- **Response Customization**: https://docs.github.com/en/copilot/concepts/response-customization
- **Premium Request Monitoring**: https://docs.github.com/en/copilot/how-tos/manage-and-track-spending/monitor-premium-requests
- **GitHub Copilot in VS Code cheat sheet**: https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features
- **GitHub Copilot in VS Code settings reference**: https://code.visualstudio.com/docs/copilot/reference/copilot-settings
- **Workspace Context - Making chat an expert in your workspace**: https://code.visualstudio.com/docs/copilot/reference/workspace-context

### Key Takeaways
- GitHub Copilot is a tool to enhance productivity, not replace expertise
- Effective prompting is a skill that improves with practice
- Different modes serve different purposes - choose wisely
- Visual context (screenshots) can dramatically improve results
- Model selection matters for complex tasks
- Monitor premium request usage to control costs

Remember: The goal is to work *with* AI as a collaborative partner, leveraging its strengths while applying your domain knowledge and creativity to build meaningful solutions.