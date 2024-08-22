# TODO List

## Changes Made (Completed Tasks)

### 1. Circular Dependency Fix for `RunManager` and `FunctionRegistry`
- [x] Implemented a two-phase initialization for `RunManager` and `FunctionRegistry`.
- [x] Ensured that `RunManager` is injected into `FunctionRegistry` only after both are initialized.
- [x] Introduced the method `initialize_function_registry()` to delay the initialization of the `FunctionRegistry` until all components are fully set up.

### 2. Initialization Order for FlexiAI Client
- [x] Fixed the initialization sequence in `FlexiAI` class.
  - [x] Initialized managers that don't depend on `RunManager` first.
  - [x] Set up `FunctionRegistry` with placeholders and deferred function loading.
  - [x] Injected `RunManager` into `FunctionRegistry` after all components are ready.
  - [x] Ensured function mappings were updated once all dependencies were correctly set.

### 3. Separation of User Functions from Core Functions
- [x] Ensured that user-defined functions are loaded dynamically from the `user_flexiai_rag/user_functions_mapping.py` file.
- [x] Registered user functions alongside core functions in `FunctionRegistry`.

### 4. Improved Logging and Debugging
- [x] Added detailed logging in initialization sequences to better trace the flow of operations.
- [x] Improved error handling in user function loading to log specific issues.

### 5. Structure Update to `FunctionsManager`
- [x] Kept `FunctionsManager` dependency injection intact using `MultiAgentSystemManager` and `RunManager`.
- [x] Refrained from directly importing these dependencies within `FunctionsManager` to maintain modularity and adhere to good design practices.

### 6. Added Starter Files for RAG and Flask App
- [x] Added `console_scripts` to generate starter files for Flexi RAG and Flexi Flask App using simple commands.

### 7. Fixed Starter Files for RAG and Flask App
- [x] Updated requirements.txt
- [x] In Flask App -> Fixed Pandoc, LaTeX, MathJax to display correct equations in chat

### 8. Fix Console Scripts for Starter Files
- [x] Fix the `console_scripts` to help users easily create starter files for Flexi RAG and Flexi Flask App with only two commands.

### 9. Add Assistant Manager for AI Assistant Operations
- [x] Introduced the `AssistantManager`, which is responsible for managing AI assistants through the OpenAI Assistants API. This includes creating, updating, retrieving, and integrating assistants into ongoing threads, allowing for more flexible and configurable AI assistant management. NOTE: Need more updates to make the parameters more flexible.



---

## Pending Tasks (To Do)

### 1. Documentation Update
- [ ] Update the documentation to reflect recent changes, including the new initialization pattern, function registrations, and other core changes.

### 2. Code Cleanup: Remove Old Functions
- [ ] Review the codebase, identify deprecated or unused functions, and remove them. Keep the essential ones.

### 3. Notebook Demonstrations
- [ ] Create demonstrations in notebooks.
- [ ] Provide examples of all basic functions and create tutorials for users.

### 4. Update Installation Video
- [ ] Record a new video showing the updated installation process, reflecting changes made in the setup.

### 5. Fix Package Dependencies
- [ ] Review and fix package dependencies.
- [ ] Ensure all necessary packages are correctly listed and managed for easy setup.

### 6. Implement Singleton Pattern for Managers
- [ ] Explore and implement the Singleton pattern for managers to ensure that only one instance of each manager exists at runtime.

### 7. Test and Fix Parallel Calling on User Side
- [ ] Test parallel tool calling on the user side and address any issues.
- [ ] Ensure that all parallel executions work as intended with user-defined functions.

### 8. Video Demonstration
- [ ] Create and add video demonstrations for Flexi Installation, 
- [ ] Create and add video demonstration for AI Alignment. (no public code here)
