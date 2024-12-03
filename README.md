# UC Expert - Ulcerative Colitis Patient Management System

UC Expert is a comprehensive Django-based web application designed to help patients with Ulcerative Colitis (UC) manage their condition effectively. It provides tools for tracking symptoms, medications, food triggers, and offers AI-powered chat support for UC-related questions which are answered solely within the context of provided information.

![Responsive Mockup](placeholder for mockup image)

## Table of Contents



## Pre-Development
<details>
<summary>The idea</summary>

### The Idea

I settled on a challenging goal: create a comprehensive Ulcerative Colitis management tool incorporating advanced AI chat capabilities through a RAG (Retrieval Augmented Generation) system. While RAG might seem "overkill" for the initial scope, it was chosen for:

- Learning opportunity in AI integration
- Future scalability for multiple medical conditions
- Potential for modular reuse
- Enhanced user support capabilities
- Control over LLM responses

### Why UC Expert?

After having conversation with the medical director of InVita intellignece, Mark Sullivan, I noticed a misalignment between doctors and their patients on a particular idea. Mark explained to me how doctors value "Expert Patients". Having a patient who understands their condition well is beneficial to the doctor, as what is reported to them tends to be more accurate and relevant. I did some research among family, friends and peers, and learned that this notion is not realised by many people suffering from some form of affliction that is regularly monitored by their doctor. They feel as though, if anything, they are pushed away from understsnding the exact workings of their condition, and are simply told what to monitor and how to do it. This can work fine for many dilligent patients, but some stated thay feel a disconnect. They want to understand their illness in depth, but may feel "stupid" when speaking to a doctor regarding recent developments in symptoms or things they may think are of note. UC expert was born of my own experience in this area and response I received from others. It aims to create expert UC patients by allowing them to interact with an AI, regarding not just general information on the disease, but specific information relating to their current symptoms and state of their condition. They can ask the "stupid" questions they may prefer not to ask their doctor, gain re-assurance on particular issues, gain a deeper understanding of what may be causing them and have a record of symptoms they can then talk more confidently with their doctor about. The AI must re-direct to a mecical professional when the users interaction warrants it.

</details>

<details>

<summary>Prototype</summary>

### Prototype Introduction

 Before I started the real project I decided to build a prototype using AI. This is a methodology I have adopted that allows me to ideate, validate, and test in a rapid and cutting edge manner. The new capabilities of LLM's and IDE's with native LLM integration allow for a this novel approach, which provides many advantages. I do initial research on the technologies required to build the app I have in mind, as you would expect. However, I then use this research to develop a comprehensive pseudocode style plan that will prompt an IDE native LLM to build the app. Once the prototype is complete I can quickly alter elements, iterate on possible features or improve existing ones, all while testing it's capabilities to see if it is performing as I expect. This allows me to interact with any product idea I have very quickly. It leads to rapid itterations and more detailed plans including refactoring before I have even written a line of code. I can then use the prototype as a basis to develop the app with minimal AI assitance, as I did with this project. It is a great way to learn a new technology. You gain an understanding of it's architecture and core pinciples without worrying about having to learn the detailed syntax of a particular function, that upon later testing turns out to be reduntant or unused by the user. 
 
 The following is an overview of how I applied this methedology prior to starting this project.


### Prototype Development Approach

#### Research Phase

- Studied RAG system implementations by watching videos and reading langchain documentation.
- Explored Django best practices and watched tutorials on django architecture and implementation.
- Investigated AI integration options (Local/API and Model choice).

#### AI-Assisted Learning

- Used Claude AI for development planning.
- Leveraged Cursor.directory for Django best practice prompts.
- Created comprehensive prompts covering:

- Django architecture
- LangChain integration
- RAG system implementation
- Tailwind CSS styling
- Database ERD

#### AI development

Used AI native Cursor IDE to develop the prototype. The main body of this took around an hour. I then developed it further by adding features and refinements until I was happy with it as a proof of concept. 

It can be found here https://github.com/GuyMitchy/Expert-Patient

#### Technical Validation

- Tested RAG using Ollama locally
- Verified basic Django structure
- Validated database relationships
- Assessed UX/UI concepts

#### Outcomes

- Gained a deeper understanding of django project architecture
- Vaildated proof of concept and viabilty as a potential capstone project candidate.
- Prototype acts as a roadmap and development guide
- Learning opportunity - Native AI with indexed codebase allows me to question "how and why" things are working as they do. Learning as the AI explains syntax and implementation details. 
- LLM monitoring and assesment - Gained a deeper understanding on the capabilty of LLM's. Upon asking for explanations you realise the mistakes it makes (usually overcomplicating things), learning from it's mistakes like I would learn from my own.
- Deeper understanding of the importance of comprehensive planning, realisation that "It's all in the planning"

Once the prototype was complete and my assemment on viabilty was made I chose to proceed with the project.

</details>

## Core Development Plan

<details>
<summary>STRATEGY</summary>

### STRATEGY

- Primary goal: Help UC patients track and manage their condition effectively by tracking symptoms, medications and Foods.
- Allow users to interact with a chatbot regarding their condition in order to become an expert patient
- Focus on creating a reliable, easy-to-use health management tool.
- Enable data-driven conversations with healthcare providers by having a record of their condition, in-place of on the spot memory recall which creates the potential for innacurate data.

#### User Needs

#### Newly Diagnosed Patients

- Understanding UC basics and terminology
- Learning to identify and track symptoms
- Getting started with medication management
- Understanding dietary impacts
- Emergency guidance for severe symptoms

#### Experienced Patients

- Detailed symptom tracking and pattern recognition
- Long-term medication management
- Food trigger identification
- Historical data analysis
- Personalized insights about their condition

#### Active Flare Management

- Immediate symptom logging
- Emergency guidance
- Dietary adjustment tracking
- Quick access to historical data

#### Remission Maintenance

- Preventive tracking
- Early warning sign identification
- Lifestyle management
- Diet optimization

### User Stories and Development Management
To efficiently manage the user story development process, I created a utility to automatically generate GitHub issues from user stories in .yaml format (https://github.com/GuyMitchy/github-user-story-populator).

This automated approach allowed for:

- Consistent issue formatting
- Automatic label application (Must Have, Should Have, etc.)
- Creation of task checkboxes for acceptance criteria
- Improved development workflow

### Must Have Features
Symptom Logging
"As a UC patient, I need to record and track my symptoms, so that I can monitor my condition's progression and share accurate information with my healthcare providers."
Assessment Criteria:

Can select from predefined symptom types
Can rate severity on a 1-5 scale
Can add descriptive notes about symptoms
Can set the date of symptoms
Can view a list of recorded symptoms
Can edit or delete existing symptom entries

#### Medication Management
"As a UC patient, I need to manage my medication regimen, so that I can maintain consistent treatment and track the effectiveness of different medications."
Assessment Criteria:

Can add new medications with name, dosage, and frequency
Can specify medication start date
Can mark medications as active/inactive
Can add notes about medications
Can view complete medication history
Can edit medication details
Can delete medication entries

#### Basic AI Chat Support
"As a UC patient, I need to get reliable information about my condition, so that I can make informed decisions about my daily health management."
Assessment Criteria:

Can start new conversations with custom titles
Can receive responses based on verified UC information
Can view chat history
Receive emergency guidance for severe symptoms
Get redirected to healthcare providers when appropriate
Can access previous conversations

#### Food Diary Management
"As a UC patient, I need to track my food intake and its effects, so that I can identify trigger foods and maintain a diet that minimizes flare-ups."
Assessment Criteria:

Can log meals with date and time
Can specify food items consumed
Can note specific reactions to foods
Can view food diary history
Can identify trigger foods through history
Can edit or delete food diary entries

#### User Authentication
"As a UC patient, I need secure access to my medical information, so that I can maintain privacy and confidentiality of my health data."
Assessment Criteria:

Can register for an account
Can log in securely
Can log out
Can only access own medical data
Has persistent data across sessions

### Should Have Features

#### Personalized AI Responses
"As a UC patient, I need the AI to understand my specific condition, so that I can receive relevant and personalized guidance for my unique situation."
Assessment Criteria:

AI references user's current medications in responses
AI considers user's symptom history when giving advice
AI provides personalized recommendations based on user data
AI maintains medical context throughout conversation
AI flags concerning symptom patterns
AI avoids contradicting user's current treatment plan

#### AI Knowledge Verification
"As a UC patient, I need to trust the AI's information, so that I can confidently use its guidance in managing my condition."
Assessment Criteria:

AI clearly indicates when information is not available
AI provides consistent answers to similar questions
AI acknowledges medical disclaimer when appropriate
AI maintains professional medical terminology
AI correctly categorizes symptom severity

#### Could Have Features
Food Pattern Analysis
"As a UC patient, I need to understand how food affects my condition, so that I can make better dietary choices and prevent symptom flare-ups."
Assessment Criteria:

Can view foods grouped by reaction severity
Can see correlation between foods and symptoms
Can mark foods as "safe" or "trigger"
Can add notes about food interactions and effects
Can track portion sizes and their effects

#### AI Chat Context Management
"As a UC patient, I need the AI to maintain conversation context, so that I can have more meaningful and coherent discussions about my health concerns."
Assessment Criteria:

AI "remembers" previous messages in conversation
AI can reference earlier parts of conversation
AI maintains consistent advice throughout chat
AI can clarify previous responses
AI can update responses based on new information

#### Won't Have Features

Medication reminders/scheduling
Direct healthcare provider communication
File upload for medical documents
Medication interaction checking
Integration with medical devices/apps
Automated meal planning
Social features or community support
Integration with electronic health records

</details>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<details>
<summary>SCOPE</summary>

### SCOPE

#### Core Features Based on User Stories

#### Authentication System
- Email-based registration and login
- Password validation and security
- Session management
- Access control to personal data

#### Dashboard Requirements
- Overview panel showing recent entries
- Quick access cards to main features:
  - Symptom logging
  - Medication management
  - Food diary
  - Chat system
- Latest entries from each tracking system
- Only shows active medications

#### Symptom Tracking System
```python
Required Fields:
- User (ForeignKey)
- Date (DateField)
- Type (CharField with choices):
    - Abdominal Pain
    - Blood in Stool
    - Urgency
    - Diarrhoea
    - Fatigue
    - Joint Pain
    - Other
- Severity (IntegerField 1-5):
    - Very Mild
    - Mild
    - Moderate
    - Severe
    - Very Severe
- Description (TextField)
```

#### Medication Management System
```python
Required Fields:
- User (ForeignKey)
- Name (CharField with categories):
    - 5-ASAs
    - Corticosteroids
    - Immunomodulators
    - Biologics
    - JAK Inhibitors
- Dosage (CharField)
- Frequency (CharField with choices):
    - Daily
    - Twice Daily
    - Three Times Daily
    - Four Times Daily
    - Weekly
    - Every Other Week
    - Monthly
    - As Needed
- Start Date (DateField)
- Active Status (BooleanField)
- Notes (TextField)
```

#### Food Diary System
```python
Required Fields:
- User (ForeignKey)
- Date (DateTimeField)
- Eaten At (TimeField)
- Meal Type (CharField):
    - Breakfast
    - Lunch
    - Dinner
    - Snack
- Food Name (CharField)
- Portion Size (CharField)
- Is Trigger (BooleanField)
- Notes (TextField)
```

### AI Chat System Requirements

#### Conversation Management
```python
Required Fields:
- User (ForeignKey)
- Title (CharField)
- Created/Updated timestamps
```

#### Message Management
```python
Required Fields:
- Conversation (ForeignKey)
- Content (TextField)
- Is Bot (BooleanField)
- Created timestamp
```

#### RAG System Requirements
- Knowledge Base Content:
  - UC medical information
  - Medication details
  - Emergency guidance
  - Dietary information
  - Lifestyle management
  
- Vector Database Requirements:
  - Document chunking (250 char chunks)
  - Chunk overlap (25 chars)
  - Embedding storage
  - Efficient retrieval

- Context Management:
  - User symptom history
  - Current medications
  - Recent food entries
  - Conversation history

### UI/UX Requirements

#### Navigation
- Fixed top navigation bar
- Mobile-responsive menu
- Quick access to main features through dashboard cards
- Consistent back navigation

#### Forms
- Clear error messages
- Input validation
- Date selection controls
- Mobile-friendly inputs

#### Lists and History Views
- Chronological ordering
- Filtering capabilities
- Clear data presentation
- Edit/Delete functionality

#### Responsive Design
- Mobile-first approach
- Tailwind breakpoints:
  - md: 768px


### Content Requirements

#### Medical Knowledge Base
- Markdown format for reliable vector storage and retrieval
- Core UC information
- Medication details and usage
- Emergency response guidance
- Dietary recommendations
- Lifestyle management advice

#### User Guidance
- Feature usage instructions
- Data entry guidelines
- Emergency information
- Privacy policies
- Terms of service

#### System Messages
- Welcome messages
- Confirmation alerts
- Error notifications
- Success feedback

#### Future Content/Features:
- Medication reminders
- Direct healthcare provider communication
- Medical document upload
- Automated meal planning
- Community support features
- Disease state report creation

</details>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


<details>
<summary>STRUCTURE</summary> 

### STRUCTURE

### Overview
- Dashboard-centered design for quick access to all features.
- Cards to decribe and navigate to each feature.
- Clear navigation to each section always available via navbar.
- Consistent layout across all features.
- Footer section providing usage information, policies and disclaimers.
- Data entry forms(add, delete and edit) for each feature
- Historical list pages for each feature.
- Chat windows for each conversation with persistent chat history.

### Site Map

#### Non-Authenticated
- Landing Page
  - Login
  - Register
  - About UC Expert
  - Privacy Policy

#### Authenticated Users

#### Header
- Logo/Brand
- Navigation Menu
- User Welcome
- Logout Option

#### Dashboard (Home)
- Recent Activity Overview
  - Latest Symptoms (3)
  - Active Medications (3)
  - Recent Foods (3)
- Quick Access Cards
  - Symptom Tracker
  - Medication Log
  - Food Diary
  - Chat with UC Expert

#### Symptom Management
- List View
  - Add new Symptom button - links to form
  - View all Symptoms in reverse order
  - Edit/Delete buttons - link to forms
  - Add confirmation
  - Delete Confirmation

#### Medication Management
- List View
  - Add New Medication button - links to form
  - View All Medications in reverse order
  - Active/Inactive Filter - shows greyed if inactive
  - Edit/Delete buttons - link to forms
  - Add confirmation
  - Delete Confirmation

#### Food Diary
- List View
  - Add New Entry - link to form
  - View All Entries in reverse order
  - Edit/Delete buttons - link to forms
  - Add confirmation
  - Delete Confirmation

#### Chat System
- List View
  - Start New Converstion
  - View Previous Conversations in reverse order
  - Delete button - links to form
- Chat Detail
  - Chat window
  - Message History
  - Message Input Area
  - Back to conversations button - links to list view

  
## Information Architecture

### Database Relationships
```
User
└── Symptoms (One-to-Many)
└── Medications (One-to-Many)
└── Foods (One-to-Many)
└── Conversations (One-to-Many)
    └── Messages (One-to-Many)
```

### View Structure
```
Views/
├── Base Views (LoginRequiredMixin)
│   ├── ListView
│   ├── CreateView
│   ├── UpdateView
│   └── DeleteView
├── Home
│   └── Dashboard View
├── Symptoms
│   ├── List
│   ├── Create
│   ├── Update
│   └── Delete
├── Medications
│   ├── List
│   ├── Create
│   ├── Update
│   └── Delete
├── Foods
│   ├── List
│   ├── Create
│   ├── Update
│   └── Delete
└── Chat
    ├── Conversation List
    ├── Conversation Detail
    ├── Create
    └── Delete
```

### Template Structure
```
Templates/
├── base.html
├── home/
│   └── dashboard.html
├── symptoms/
│   ├── list.html
│   ├── add.html
│   ├── edit.html
│   └── delete.html
├── medications/
│   ├── list.html
│   ├── add.html
│   ├── edit.html
│   └── delete.html
├── foods/
│   ├── list.html
│   ├── add.html
│   ├── edit.html
│   └── delete.html
└── chat/
    ├── list.html
    ├── detail.html
    ├── new_conversation.html
    ├── delete.html
    └── message.html
```

### RAG System Architecture
```
knowledge/
├── manager.py (Singleton Pattern)
│   ├── RAGManager
│   │   ├── _instance (Single RAG instance)
│   │   ├── get_instance() (Get/create RAG instance)
│   │   └── cleanup() (Resource management)
│   └── with_rag decorator (Handles RAG instance injection)
│
├── rag_setup.py (System Configuration)
│   └── UCExpertRAG
│       ├── __init__
│       │   ├── OpenAI embeddings setup
│       │   ├── Pinecone vector store initialization
│       │   └── Chat prompt template configuration
│       ├── initialize_documents()
│       │   ├── Document loading
│       │   ├── Text splitting (250 char chunks)
│       │   └── Vector store population
│       ├── get_diverse_documents()
│       │   └── Similarity search functionality
│       └── get_response()
│           ├── Context building
│           ├── Response generation
│           └── Error handling
│
└── docs/
    └── core_knowledge.md
        ├── Emergency Information
        ├── Symptoms
        ├── Monitoring
        ├── Diet
        ├── Lifestyle
        ├── Support
        └── Medications
```

### RAG System Data Flow
1. Initialization
   ```python
   # Single instance creation via decorator
   @with_rag
   def send_message(request, conversation_id, rag=None):
       # rag parameter automatically injected
   ```

2. Knowledge Processing
   ```python
   # Document processing
   text_splitter = RecursiveCharacterTextSplitter(
       chunk_size=250,
       chunk_overlap=25,
       separators=["\n## ", "\n### ", "\n", " ", ""]
   )
   ```

3. Context Building
   ```python
   # User context structure
   user_context = """
   User Context:
   - Recent Symptoms
   - Current Medications
   - Food Diary Entries
   
   Conversation History:
   - Previous Messages
   """
   ```

4. Response Generation Pipeline
```mermaid
graph TD
    %% Entry Point
    Start[/User Sends Message/]:::blackText --> Decorator[with_rag Decorator]:::blackText
    Decorator --> CheckInstance{RAG Instance <br/>Exists?}:::blackText
    
    %% RAGManager Singleton
    CheckInstance -->|No| Init[Initialize UCExpertRAG]:::blackText
    Init --> InitEmbed[Setup OpenAI Embeddings]:::blackText
    InitEmbed --> InitLLM[Initialize ChatGPT]:::blackText
    InitLLM --> InitPine[Connect to Pinecone]:::blackText
    InitPine --> DefinePrompt[Define Base Prompt Template]:::blackText
    DefinePrompt --> CheckVS{Vector Store Empty?}:::blackText
    
    CheckVS -->|Yes| LoadDocs[Load Documents]:::blackText
    LoadDocs --> SplitDocs[Split Documents]:::blackText
    SplitDocs --> CreateEmbed[Create Embeddings]:::blackText
    CreateEmbed --> StoreVecs[Store in Pinecone]:::blackText
    StoreVecs --> RAGInstance[RAG Instance Ready]
    
    CheckVS -->|No| RAGInstance
    CheckInstance -->|Yes| RAGInstance
    
    %% Query Processing
    RAGInstance --> SimSearch[Similarity Search]:::blackText
    SimSearch --> RetrieveContext[Retrieve Relevant Documents]:::blackText
    
    %% Context Building in Parallel
    RAGInstance --> BuildContext[Build User Context]:::blackText
    BuildContext --> GetSymptoms[Get Recent Symptoms]:::blackText
    BuildContext --> GetMeds[Get Active Medications]:::blackText
    BuildContext --> GetFood[Get Food Diary]:::blackText
    BuildContext --> GetHistory[Get Chat History]:::blackText
    
    %% Combine Everything
    RetrieveContext --> FormatPrompt[Format Complete Prompt]:::blackText
    BuildContext --> FormatPrompt
    FormatPrompt --> CombineElements[Combine:<br/>1. Base Template<br/>2. Retrieved Context<br/>3. User Context<br/>4. Chat History<br/>5. User Question]:::blackText
    CombineElements --> SendToLLM[Send to ChatGPT]:::blackText
    SendToLLM --> SaveMsg[Save Message]:::blackText
    SaveMsg --> End[/End/]:::blackText
    
    %% Styling
    classDef init fill:#e1f5fe,stroke:#01579b
    classDef singleton fill:#f3e5f5,stroke:#4a148c
    classDef context fill:#fff3e0,stroke:#e65100
    classDef process fill:#e8f5e9,stroke:#1b5e20
    classDef prompt fill:#fce4ec,stroke:#880e4f
    classDef blackText color:black
    
    class Start,End process
    class Decorator,CheckInstance,Init,InitEmbed,InitLLM,InitPine singleton
    class CheckVS,LoadDocs,SplitDocs,CreateEmbed,StoreVecs init
    class BuildContext,GetSymptoms,GetMeds,GetFood,GetHistory context
    class DefinePrompt,FormatPrompt,CombineElements prompt
    class SimSearch,RetrieveContext,SendToLLM,SaveMsg process

    
```

5. Resource Management
   ```python
   # Cleanup on shutdown
   atexit.register(RAGManager.cleanup)
   ```

6. Error Handling
   ```python
   try:
       response = rag.get_response(
           question=user_message,
           user_info=user_context,
           conversation_history=conversation_history
       )
   except Exception as e:
       # Error handling and logging
   ```


### User Flow
1. Authentication
   - Register/Login
   - Redirect to Dashboard

2. Dashboard Navigation
   - Overview of recent data
   - Access to main features

3. Feature Workflows
   - List View Entry
   - Create New Entry
   - View/Edit Details
   - Delete Confirmation

4. Chat Interaction
   - Start/Continue Conversation
   - Receive Contextual Responses
   - Emergency Guidance When Needed



</details>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<details>

<summary>SKELETON</summary>

## SKELETON

### Wireframes

![Desktop](static/readme_images/desktop_wireframe.png)

![Mobile](static/readme_images/mobile_wireframe.png)

### ERD

```mermaid
erDiagram
    User ||--o{ Symptom : logs
    User ||--o{ Medication : manages
    User ||--o{ Conversation : has
    User ||--o{ FoodDiary : records
    Conversation ||--o{ Message : contains

    User {
        int id PK
        string username
        string email
        string password
    }

    Symptom {
        int id PK
        int user_id FK
        date date
        string type
        int severity
        text description
    }

    Medication {
        int id PK
        int user_id FK
        string name
        string dosage
        string frequency
        date start_date
        boolean active
        text notes
        datetime created_at
        datetime updated_at
    }

    FoodDiary {
        int id PK
        int user_id FK
        datetime eaten_at
        string meal_type
        string food_name
        string portion_size
        boolean is_trigger
        text notes
        datetime created_at
        datetime updated_at
    }

    Conversation {
        int id PK
        int user_id FK
        string title
        datetime created_at
        datetime updated_at
    }

    Message {
        int id PK
        int conversation_id FK
        text content
        boolean is_bot
        datetime created_at
    }
   ```

### Interactive Elements

#### Buttons
- Primary Actions (Add, edit, save)
- Secondary Actions (Cancel, Back)
- Destructive Actions (Delete)
- Icon Buttons (Edit, Delete)

#### Forms
- Text Inputs
- Select Dropdowns
- Date/Time Pickers
- Checkboxes
- Text Areas

### Feedback Elements
- Success Messages
- Error Alerts
- Loading States
- Confirmation Dialogs

</details>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<details>

<summary>SURFACE</summary>

## SURFACE

### Overview

- Medical-inspired blue color scheme for professionalism and trust
- High contrast for readability
- Clear visual feedback for user actions
- Consistent use of Tailwind CSS for styling
- Familiar chat window with colour coded message boxes

### Visual Design Elements

#### Color Palette
```css
Primary Colors:
- Medical Blue: #2563eb (Tailwind blue-600)
- White: #ffffff
- Success Green: #16a34a (Tailwind green-600)
- Warning Yellow: #ca8a04 (Tailwind yellow-600)
- Error Red: #dc2626 (Tailwind red-600)

Background Colors:
- Light Gray: #f3f4f6 (Tailwind gray-100)
- Card White: #ffffff
- Hover States: #1d4ed8 (Tailwind blue-700)

Message Colors:
- Bot Message: #dbeafe (Tailwind blue-100)
- User Message: #dcfce7 (Tailwind green-100)
```

#### Typography
Using Tailwind's default font stack:
```css
- Headings: font-bold
- Body Text: font-normal
- Navigation: font-medium
- Form Labels: font-medium
```

#### Component Styling

##### Cards
- White background
- Shadow effect
- Rounded corners
- Hover state with increased shadow
- Transition effects

##### Forms
- Input fields with rounded borders
- Focus states with blue outline
- Clear error states with red highlighting
- Success states with green confirmation

##### Buttons
Primary:
- Blue background
- White text
- Hover darkening
- Rounded corners

Secondary:
- White background
- Gray border
- Blue text
- Hover background light blue

Destructive:
- Red background
- White text
- Hover darkening


#### Feedback Design

##### Success Messages
- Green background
- Check icon
- Temporary display
- Fade transition


##### Error Messages
- Red text


### Responsive Behavior

#### Mobile Adaptations
- Stack layouts vertically
- Simplify navigation to burger menu

#### Desktop Enhancements
- Multi-column layouts
- Hover effects
- Extended navigation

### Accessibility Considerations

#### Color Contrast
- All text meets WCAG 2.1 requirements
- Clear distinction between interactive elements
- No color-only information indicators

#### Interactive Elements
- Clear focus states
- Adequate sizing for touch targets
- Consistent interaction patterns

#### Text Readability
- Sufficient font sizes
- Adequate line spacing
- Proper contrast ratios


</details>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Deployed

<details>
<summary>Existing Features</summary>

### Existing Features

#### Authentication and user accounts

- Persistent user accounts with authentication
- Register as a new user with password verification
- Sign out page with confirmation

#### Navigation Bar

- Permanent navigation bar with links to dashboard and all list pages for each feature.

#### Dashboard
- Overview of recent symptoms, medications, and food entries
- Quick access cards to main features
- Status indicators for active medications and recent symptoms

#### Symptom Tracking
- Log symptoms with type, severity, and description
- Date-based tracking
- Visual severity indicators
- Edit and delete functionality
- Historical list view of symptoms

#### Medication Management
- Comprehensive medication database
- Track active and previous medications
- Record dosage and frequency
- Medication history view
- Edit and delete functionality

#### Food Diary
- Log meals with date and time
- Identify trigger foods
- Track portion sizes
- Add notes about reactions
- View food history
- Edit and delete functionality

#### AI Chat Support
- UC-specific knowledge base
- Context-aware responses
- Emergency guidance for severe symptoms
- Conversation history as context
- Personalized responses based on user data

</details>

<details>

<summary>Features Left to Implement</summary>

### Features Left to Implement

- Medication reminders/scheduling (Rag system can currently work out when medication should be taken based on frequency and start date)
- Direct healthcare provider communication
- File upload for medical documents
- Medication interaction checking
- Automated meal planning
- Social features/community support
- Integration with electronic health records
- Symtom report creation

</details>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


<details>
<summary>Version Control</summary>

### Version Control

#### Branching Strategy

LIST BRANCHES HERE

</details>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<details>
<summary>Agile Methedology<summary>

TALK ABOUT HOW AGILE WAS USED HERE

</details>




## Testing

### Manual Testing
Comprehensive testing is planned to include:
- Cross-browser compatibility
- Responsive design verification
- Form validation
- Data persistence
- AI chat functionality
- Security testing

### Known Issues and Resolutions

#### Resolved Issues
1. Form handling optimization
   - Initial issue: Form logic in templates was messy and causing type errors where choices were used in database fields
   - Solution: Implemented "fat models, skinny views, stupid templates" pattern. Moving logic from templates into forms.py
   - Result: Improved code organization, seperation of concerns, maintainability and readabilty.

2. Vector Database Migration
   - Initial issue: ChromaDB performance on Heroku was casuing multiple instances of the database to be created, increasing memory usage for each site access.
   - Solution: Migrated to Pinecone and vector database cleanup.
   - Result: Improved reliability and scalability

3. Slow inital load time
   - Initial issue: Website was slow to load home page due to vector database intialisition on access.
   - Solution: Moved database intialisation to send message function.
   - Result: Improved code organization, seperation of concerns, maintainability and readabilty.
   - Future improvement: Move RAG initialisation to chat window load to decrease wait time for first message response.


#### Current Limitations
- [To be added based on testing]

## Deployment

The application was deployed on Heroku using the following method:

1. Prerequisites:
   - GitHub account
   - Heroku account
   - OpenAI API key
   - Pinecone account and API key

2. Intial sStup:
   - Configure GitHub integration in Heroku dashboard
   - Set up Postgres database through Code institute
   - Configure Pinecone vector database

2. Environment Variables Required:
   - OPENAI_API_KEY
   - SECRET_KEY
   - DATABASE_URL
   - PINECONE_API_KEY

3. Procfile and runtime

3. Deployment Steps:
   - Set debug to false - I used this .env check to automate this:
   
   ```python
   DEBUG = os.path.exists('.env')
   print(f"Debug mode is set to: {DEBUG}")
   ```
   
   ```bash
   # Login to Heroku CLI
   heroku login

   # Set environment variables
   heroku config:set OPENAI_API_KEY=your_key
   heroku config:set SECRET_KEY=your_key
   heroku config:set PINECONE_API_KEY=your_key
   heroku config:set DATABASE_URL=your_key

   # Deploy
   git push heroku main
   ```

The live site can be found here: [Link to be added]

## Credits

### Technical Implementation
- Django web framework
- Tailwind CSS for styling
- OpenAI API for chat functionality
- Pinecone for vector database
- Lucide icons for UI elements

### AI Assistance
- Prototype development
- Ideation and problem-solving
- Helped with RAG system development
- Assisted in debugging and optimization

### Tools and Libraries
- Django AllAuth for authentication
- WhiteNoise for static file serving
- dj-database-url for database configuration
- python-dotenv for environment management

## Planning and Development Process

The development followed an iterative approach:

1. Initial Prototype
   - Built using Ollama for RAG testing
   - Validated core functionality
   - Identified potential challenges

2. Production Development
   - Migrated to OpenAI for improved reliability
   - Implemented user authentication
   - Developed core tracking features
   - Integrated Pinecone for vector storage

3. Deployment Optimization
   - Resolved hosting challenges
   - Optimized database interactions
   - Implemented security best practices

The project uses Django's "fat models, skinny views, stupid templates" philosophy for clean, maintainable code.


Bugs/future 

When you edit any entry all of the original data isnt shown in form so you have to add fields again. Edit should show all current data then allow user to edit any part they want. 
