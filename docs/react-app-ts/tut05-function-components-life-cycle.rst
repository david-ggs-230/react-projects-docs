.. _tut05-function-components-life-cycle:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Function Component - Life Cycle
##################################################################################################

Life Cycle Stages of each React class component:
    
    - Mounting
        - constructor()
        - getDerivedStateFromProps()
        - render()
        - componentDidMount()
    - Updating
        - shouldComponentUpdate()
        - getDerivedStateFromProps()
        - render()
        - getSnapshotBeforeUpdate()
        - componentDidUpdate()
    - Unmounting
        - componentWillUnmount()
        

In React, function components don't have lifecycle methods like class components do (e.g., componentDidMount, componentDidUpdate, componentWillUnmount). However, you can simulate lifecycle behavior using React hooks, specifically useEffect. Here’s how the lifecycle equivalents in function components work:
    
    - componentDidMount Equivalent (Runs once after the component mounts): In class components, componentDidMount is called once the component is mounted (i.e., after the component is rendered to the screen).
        
        - In functional components, the useEffect hook with an empty dependency array [] runs once when the component is mounted. This simulates the componentDidMount behavior. ::
            
            useEffect(() => {
              // This runs once, after the component mounts
              console.log("Component mounted");
            }, []); // Empty array means it runs only once
            
    - componentDidUpdate Equivalent (Runs when the component updates): In class components, componentDidUpdate is called after every update, i.e., whenever the component re-renders due to a change in state or props.
        
        - In functional components, the useEffect hook with a dependency array runs whenever the values in that array change. This simulates the componentDidUpdate behavior. ::
            
            useEffect(() => {
              // This runs after every update (re-render)
              console.log("Component updated");
            }, [count]); // Runs whenever 'count' changes
            
    - componentWillUnmount Equivalent (Runs before the component unmounts): In class components, componentWillUnmount is called right before a component is unmounted and destroyed. It is used for cleanup.
        
        - In functional components, you can achieve this behavior by returning a cleanup function from the useEffect hook. This cleanup function will run when the component unmounts, which will act like componentWillUnmount. ::
            
            useEffect(() => {
              // This is the effect setup code
              return () => {
                  // This cleanup code runs when the component unmounts
                  console.log("Component will unmount");
              };
            }, []); // Empty array means the effect runs once (on mount) and cleanup runs on unmount
            
    - getDerivedStateFromProps Equivalent in Function Components: This method is used in class components to update state based on props changes.
        
        - For function components, there isn't a direct equivalent to getDerivedStateFromProps, but you can achieve similar behavior using the useEffect hook in combination with the state and props. 
        - In functional components, you generally manage state changes directly with useState, and you can conditionally update the state based on props or any other factors. 
        - getDerivedStateFromProps can return null if no state update is needed, whereas useEffect doesn't return a value but can conditionally perform a state update if necessary. ::
            
            function MyComponent({ propValue }) {
              const [stateValue, setStateValue] = useState(propValue);
            
              useEffect(() => {
                // This effect simulates the behavior of getDerivedStateFromProps
                if (propValue !== stateValue) {
                  setDerivedValue(propValue); // Update the state when the prop changes
                }
              }, [propValue]); // The effect runs when `propValue` prop changess
            
              return <div>{stateValue}</div>;
            }
            
    - shouldComponentUpdate Equivalent Using React.memo: In class components, the shouldComponentUpdate lifecycle method is used to control whether a component should re-render or not when its props or state change. It returns a boolean indicating whether React should proceed with the re-render (true) or skip it (false).
        
        - For function components, React doesn't have an exact equivalent of shouldComponentUpdate, but you can achieve similar behavior using the React.memo higher-order component (HOC). React.memo helps you optimize performance by preventing unnecessary re-renders when the props of the component don't change.
        - Additionally, if you want more control over when the component should re-render, you can use the useCallback and useMemo hooks inside the function component to memoize functions or values and avoid unnecessary re-renders.
        - React.memo is the simplest and most common way to achieve a shouldComponentUpdate equivalent in function components. It compares the previous props with the new props and only re-renders the component if the props have changed. ::
            
            import React, { useState } from 'react';
            
            const MyComponent = React.memo(({ count }) => {
              console.log('Rendering MyComponent');
              return <div>{count}</div>;
            }, (prevProps, nextProps) => {
              // Only re-render if 'count' prop changes
              return prevProps.count === nextProps.count;
              // Return true if props are equal and re-render should be prevented
              // Return false if props are different and re-render should occur
            });
            
            export default MyComponent;
            
        - In the example above:
            
            - React.memo wraps the functional component.
            - The second argument to React.memo is a function that compares the previous and next props. If the function returns true, the component will not re-render. If it returns false, the component will re-render.
            
    
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-life-cycle --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-life-cycle> ::
        
        cd tut05-function-components-life-cycle
        
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
Create Lifecycle Equivalents in Function Components
**************************************************************************************************

==================================================================================================
Function Components with Life Cycle Equivalents
==================================================================================================

    
    Define a function component with life cycle equivalents.
        
        .. code-block:: tsx
          :caption: src/FunctionalComponentLifeCycleEquivalents.tsx
          :linenos:
          
          import React, { useState, useEffect } from "react";
          
          const FunctionalComponentLifeCycleEquivalents: React.FC = () => {
            const [count, setCount] = useState(0);
            const logMessagesRef = React.useRef([] as string[]);
          
            // Equivalent to Component first mount and componentWillUnmount
            useEffect(() => {
              const logMessages = logMessagesRef.current;
              logMessages.push("Component first mount");
              logMessagesRef.current = logMessages;
              return () => {
                const logMessage = `Equivalent: componentWillUnmount()`;
                logMessages.push(logMessage);
                logMessagesRef.current = logMessages;
              };
            }, []);
            // Equivalent to componentDidMount and componentDidUpdate
            useEffect(() => {
              const logMessage = `Equivalent: componentDidMount() / componentDidUpdate(), count: ${count}`;
              logMessagesRef.current.push(logMessage);
            }, [count]);
          
            const handleIncrement = () => {
              setCount(count + 1);
              const logMessage = `handleIncrement(), count: ${count + 1}`;
              logMessagesRef.current.push(logMessage);
            };
          
            return (
              <>
                <div className="list-container">
                  <h2>Function Component Life Cycle</h2>
                  <p>
                    Count: {count} <button onClick={handleIncrement}>Increment</button>
                  </p>
                  <h4>Log Messages:</h4>
                  <ol>
                    {logMessagesRef.current.map((message, index) => (
                      <li key={index} className="list-item" style={{ margin: "1px" }}>
                        <div>
                          {index + 1}. {message}
                        </div>
                      </li>
                    ))}
                  </ol>
                </div>
              </>
            );
          };
          
          export default FunctionalComponentLifeCycleEquivalents;
          
          
==================================================================================================
Create a Function Component to Show the User Interface
==================================================================================================
    
    Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import FunctionalComponentLifeCycleEquivalents from "./FunctionalComponentLifeCycleEquivalents";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return <FunctionalComponentLifeCycleEquivalents />;
          };
          
          export default FunctionComponentsDisplay;
          
    - Edit ``App.tsx`` to render the component
        
        .. code-block:: tsx
          :caption: src/App.tsx
          :linenos:
          
          import FunctionComponentsDisplay from "./FunctionComponentsDisplay";
          import "./App.css";
          
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
          
**************************************************************************************************
Hosting the React App on GitHub Pages
**************************************************************************************************

==================================================================================================
Build the App
==================================================================================================
    
    - Configure the build base url:
        
        - open vite.config.js file
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-life-cycle/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-life-cycle/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-life-cycle/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-life-cycle/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-life-cycle/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-life-cycle
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-life-cycle/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-life-cycle.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Function Components - Life Cycles
           
           :custom-color-primary-bold:`React Function Components - Life Cycles`