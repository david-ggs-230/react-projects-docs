.. _tut05-function-components-state:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Function Components - State
##################################################################################################

In React components, state is used to store and manage data that can change over time within the component. The state allows a component to keep track of information between renders and update the user interface (UI) when the state changes.

In React, function components can have state using the useState hook. The useState hook allows you to add state variables to function components, making them dynamic and interactive. 
    
    - State in Function Components is managed using the useState hook.
    - The hook returns an array: the first element is the current state value, and the second element is a function used to update the state.
    - Whenever the state changes, the component re-renders to reflect the new state.
    
A React function component manages and exposes its state through the useState hook. When the state is updated, the component triggers a re-render to reflect the changes in the UI.
    
    - State vs Props in Function Components:
        
        - State is used for data that can change over time and is local to the component.
        - Props are used to pass data from parent components to child components and are immutable inside the child component.
        
    
    - Key Concepts of State in React Function Components:
        
        - State is local to the component: Each instance of a function component has its own state, and it is not shared with other components unless explicitly passed down as props.
        - State is mutable: Unlike props, the state of a component can be changed over time.
        - State changes trigger re-renders: When the state changes, React re-renders the component to reflect the updated state in the UI.
        
    - How to Use State in React Function Components:
        
        - Initialize State: the useState hook is called with an initial state value.
        - Access State: The useState hook returns an array with two elements: The first element is the variable that stores the current state value used to access the state.
        - Update State: The useState hook returns an array with two elements: The second element is a function used to update the state.
        
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-state --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-state> ::
        
        cd tut05-function-components-state
        
    - Install the dependencies ::
        
        yarn install
        
==================================================================================================
ESLint and Prettier Configuration
==================================================================================================
    
    - Install the ``EditorConfig`` extension for VS Code if you haven't already.
    - Add .editorconfig (https://editorconfig.org) to the root of the project
        
        .. code-block:: cfg
          :caption: contents of .editorconfig
          :linenos:
          
          root = true
          
          [*]
          indent_style = space
          indent_size = 2
          end_of_line = lf
          insert_final_newline = true
          trim_trailing_whitespace = true
          
    - Reload VS Code (open the command palette, find and use ``Reload Window``).
    - Install dependencies ::
        
        yarn add --dev prettier eslint-plugin-prettier eslint-config-prettier eslint-plugin-react
        
    - Modify the eslint.config.js file with following contents:
        
        .. code-block:: js
          :caption: contents of eslint.config.js
          :linenos:
          
          import js from "@eslint/js";
          import globals from "globals";
          import reactHooks from "eslint-plugin-react-hooks";
          import reactRefresh from "eslint-plugin-react-refresh";
          import tseslint from "typescript-eslint";
          import react from "eslint-plugin-react";
          import eslintPluginPrettier from "eslint-plugin-prettier/recommended";
          
          export default tseslint
            .config(
              { ignores: ["dist"] },
              {
                //extends: [js.configs.recommended, ...tseslint.configs.recommended],
                extends: [
                  js.configs.recommended,
                  ...tseslint.configs.recommendedTypeChecked,
                ],
                files: ["**/*.{ts,tsx}"],
                languageOptions: {
                  ecmaVersion: 2020,
                  globals: globals.browser,
                  parserOptions: {
                    project: ["./tsconfig.node.json", "./tsconfig.app.json"],
                    tsconfigRootDir: import.meta.dirname,
                  },
                },
                settings: {
                  react: {
                    version: "detect",
                  },
                },
                plugins: {
                  "react-hooks": reactHooks,
                  "react-refresh": reactRefresh,
                  react: react,
                },
                rules: {
                  ...reactHooks.configs.recommended.rules,
                  "react-refresh/only-export-components": [
                    "warn",
                    { allowConstantExport: true },
                  ],
                  ...react.configs.recommended.rules,
                  ...react.configs["jsx-runtime"].rules,
                },
              },
            )
            .concat(eslintPluginPrettier);
          
    - Edit the eslint scripts in the package.json file: 
        
        .. code-block:: cfg
          :caption: contents of package.json
          :linenos:
          
          "scripts": {
            ... ,
            "lint": "eslint src ./*.js ./*.ts --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
            "lint:fix": "eslint src ./*.js ./*.ts --ext ts,tsx --fix",
          },
          
    - Run ESLint:
        
        .. code-block:: sh
          :linenos:
          
          yarn lint
          yarn lint:fix
          
        
==================================================================================================
Create Project CSS Styles
==================================================================================================
    
    Create the src/list-styles.css file with the following contents: 
        
        .. code-block:: css
          :caption: src/list-styles.css
          :linenos:
          
          .list-container {
            max-width: 800px;
            width:max-content;
            margin: 0 auto;
            font-family: Arial, sans-serif;
          }
          
          ol {
            padding-left: 0;
            counter-reset: list-counter;
          }
          
          .list-item {
            display: flex;
            align-items: center;
            margin: 10px 0;
          }
          
          .list-item div button {
            border-radius: 8px;
            border: 1px solid rgb(90, 95, 82);
          }
          .list-item-number {
            font-weight: bold;
            margin-right: 10px;
            counter-increment: list-counter;
          }
          
          .list-item-number::before {
            content: counter(list-counter) ". ";
          }
          
          .list-item-content {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            background-color: #f9f9f9;
            flex-grow: 1;
          }
          
          .list-item-content h3 {
            margin: 0;
            font-size: 1em;
          }
          
          .list-item-content p {
            margin: 5px 0;
            font-size: 0.9em;
          }
          
          .red-color {
            color: #ff0000;
          }
          
          .blue-color {
            color: #0011ff;
          }
          
          .bg-red {
            background-color: #ff0000;
          }
          
          .bg-blue {
            background-color: #0011ff;
          }
          
**************************************************************************************************
Create Function Components Using State
**************************************************************************************************

To demonstrate the usage of state in React function components with a parent counter and a child counter, we will create two function components:
    
    - The parent component will hold the state for the counter, and it will pass that state to the child component as props. Parent Component (ParentCounter):
        
        - The parent has its own counter (parentCounter) managed via the state.
        - It has a method handleParentBtnClick to update the parent’s counter (parentCounter) when the button is clicked.
        - The parent passes its counter to the child via props (parentCounter).
        
    - The child component can modify the counter via a method provided by the parent. Child Component (ChildCounter):
        
        - The child maintains its own counter (childCounter) in the state (childCounter).
        - The child can increment its counter independently of the parent's counter by clicking the button.
        - The child has a method passed down by the parent as a prop to update the parent’s counter when the button is clicked.
        - The child's counter is updated via its own state update function, while the parent's counter is passed down as a prop.
        
==================================================================================================
Create a Function Component with State Data
==================================================================================================
    
    Define a function component with a state counter and a method to increment the counter.
        
        .. code-block:: tsx
          :caption: src/ParentComponentNoChild.tsx
          :linenos:
          
          import React from "react";
          
          const ParentComponentNoChild = () => {
            // Declare state with the useState hook
            const [parentCounter, setParentCounter] = React.useState(0);
          
            // Increment function
            const handleParentBtnClick = () => {
              setParentCounter((prevState) => prevState + 1);
            };
          
            return (
              <>
                <div style={{ marginTop: "20px" }}>
                  Parent Counter: {parentCounter}
                  <button
                    onClick={handleParentBtnClick}
                    style={{
                      display: "inline",
                      marginLeft: "20px",
                    }}
                  >
                    Increment
                  </button>
                </div>
              </>
            );
          };
          
          export default ParentComponentNoChild;
          
          
==================================================================================================
Create a Function Component Passing State Data to Child
==================================================================================================
    
    Define a function component with a state counter and a method to increment the counter, and passing the state counter and method to its child.
        
        .. code-block:: tsx
          :caption: src/ParentComponentWithChild.tsx
          :linenos:
          
          import React from "react";
          import ChildComponent from "./ChildComponent";
          
          const ParentComponentWithChild = () => {
            // Declare state with the useState hook
            const [parentCounter, setParentCounter] = React.useState(0);
          
            // Increment function
            const handleParentBtnClick = () => {
              setParentCounter((prevState) => prevState + 1);
            };
            return (
              <>
                <h5 className="blue-color" style={{ marginBottom: "0px" }}>
                  Parent: update its own counter
                </h5>
                <div style={{ marginTop: "0px" }}>
                  Parent Counter in Parent: {parentCounter}
                  <button
                    onClick={handleParentBtnClick}
                    style={{
                      display: "inline",
                      marginLeft: "20px",
                    }}
                  >
                    In Parent: Parent ++
                  </button>
                </div>
                <h5 className="blue-color" style={{ marginBottom: "0px" }}>
                  Child: update its own counter & its parent counter
                </h5>
                <ChildComponent
                  parentCounter={parentCounter}
                  handleParentCounter={handleParentBtnClick}
                />
              </>
            );
            return (
              <>
                <div style={{ marginTop: "20px" }}>
                  Parent Counter: {parentCounter}
                  <button
                    onClick={handleParentBtnClick}
                    style={{
                      display: "inline",
                      marginLeft: "20px",
                    }}
                  >
                    Increment
                  </button>
                </div>
              </>
            );
          };
          
          export default ParentComponentWithChild;
          
==================================================================================================
Create a Function Component Receiving State Data from Parent
==================================================================================================
    
    Define a function component with a state counter and a method to increment the counter, and receiving the parent's state counter and update method as props.
        
        .. code-block:: tsx
          :caption: src/ChildComponent.tsx
          :linenos:
          
          import React from "react";
          
          const ChildComponent: React.FC<{
            parentCounter: number;
            handleParentCounter: () => void;
          }> = ({ parentCounter, handleParentCounter }) => {
            // Declare state with the useState hook
            const [childCounter, setChildCounter] = React.useState(0);
          
            // Increment function
            const handleChildBtnClick = () => {
              setChildCounter((prevState) => prevState + 1);
            };
            return (
              <div style={{ marginTop: "0px" }}>
                <div>Parent Counter in Child: {parentCounter}</div>
                <div>Child Counter in Child: {childCounter}</div>
                <div>
                  <button
                    onClick={handleParentCounter}
                    style={{
                      display: "inline",
                      marginLeft: "20px",
                    }}
                  >
                    In Child: Parent ++
                  </button>
                  <button
                    onClick={handleChildBtnClick}
                    style={{
                      display: "inline",
                      marginLeft: "20px",
                    }}
                  >
                    In Child: Child ++
                  </button>
                </div>
              </div>
            );
          };
          
          export default ChildComponent;
          
==================================================================================================
Create a Function Component to Show the User Interface
==================================================================================================
    
    Create a function Component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import ParentComponentNoChild from "./ParentComponentNoChild";
          import ParentComponentWithChild from "./ParentComponentWithChild";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>Using State in a React Function Component</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Parent Counter -- No Child</h3>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Parent: update its own counter
                      </h5>
                      <div>
                        <ParentComponentNoChild />
                      </div>
                    </div>
                  </li>
          
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Parent Counter -- With Child</h3>
                      <div>
                        <ParentComponentWithChild />
                      </div>
                    </div>
                  </li>
                </ol>
              </div>
            );
          };
          
          export default FunctionComponentsDisplay;
          
    - Edit ``App.tsx`` to render the component
        
        .. code-block:: tsx
          :caption: src/App.tsx
          :linenos:
          
          import FunctionComponentsDisplay from "./FunctionComponentsDisplay";
          import "./App.css";
          import "./list-style.css";
          
          function App() {
            return <FunctionComponentsDisplay />;
          }
          
          export default App;
          
**************************************************************************************************
Run the development app
**************************************************************************************************
    
    - Run dev
        
        .. code-block:: sh
          :linenos:
          
          yarn dev
          
    - Build
        
        .. code-block:: sh
          :linenos:
          
          yarn build
          
**************************************************************************************************
Hosting the React App on GitHub Pages
**************************************************************************************************

==================================================================================================
Build the App
==================================================================================================
    
    - Configure the build base url:
        
        - open vite.config.js file
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-state/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-state/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-state/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-state/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-state/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-state
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-state/
    - Screenshot
        
        .. figure:: images/tut04/tut04-class-components-state.png
           :align: center
           :class: sd-my-2
           :width: 80%
           :alt: React Function Components - State
           
           :custom-color-primary-bold:`React Function Components - State`