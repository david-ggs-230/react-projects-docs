.. _tut05-function-components-hooks-usestate:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Hooks - useState
##################################################################################################

useState is a basic React hook, which allows a function component to maintain its own state and re-render itself based on the state changes. useState returns an array with two values: the current state value and a function to update that state. The signature of the useState is as follows
    
    - const [ <state>, <setState> ] = useState( <initialValue> )
        
        - initialValue − Initial value of the state. state can be specified in any type (number, string, array and object).
        - state − Variable to represent the value of the state.
        - setState − Function variable to represent the function to update the state returned by the useState.
        - useState accepts a function parameter instead of initial value and execute the function only once during initial rendering of the component. This will help to improve the performance, if the computation of initial value is expensive. signature: const [ <state>, <setState> ] = useState(() => { ... ; return <initialValue>; })
        
The signature of the setState function is as follows ::
    
    setState( <valueToBeUpdated> )
    
The sample usage to set and update the user's name is as follows ::
    
    // initialize the state
    const [name, setName] = useState('John')
    
    // update the state
    setName('Peter)
    
useState with Function Parameter ::
    
    const [val, setVal] = useState(() => {
       var initialValue = null
       // expensive calculation of initial value
       return initialValue
    })
    
Batches multiple state updates − Multiple state updates are batched and processed by React internally. If multiple state update has to be done immediately, then the special function flushSync provided by React can be used, which will immediately flush all the state changes. ::
    
    flushSync(() => setName('Peter'))
    
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-hooks-usestate --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-hooks-usestate> ::
        
        cd tut05-function-components-hooks-usestate
        
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
Component - useState
**************************************************************************************************

==================================================================================================
Function Components - the useState Hook
==================================================================================================

    
    Define a function component with the useState hook.
        
        .. code-block:: tsx
          :caption: src/ComponentUseState.tsx
          :linenos:
          
          import "./list-style.css";
          import { useState } from "react";
          
          const ComponentUseState = () => {
            // Declare state with the useState hook
            const [counter, setCounter] = useState(0);
            const [counter2, setCounter2] = useState(() => {
              return 0;
            });
            // Increment function
            const handleBtnClick = () => {
              setCounter((prevState) => prevState + 1);
            };
            // Increment function
            const handleBtn2Click = () => {
              setCounter2((prevState) => prevState + 1);
            };
            return (
              <>
                <div>
                  <h5
                    className="blue-color"
                    style={{ marginTop: "20px", marginBottom: "0px" }}
                  >
                    <div>useState with an initial value: </div>
                    <div>{"useState(0)"}</div>
                  </h5>
                </div>
                <div style={{ marginTop: "0px" }}>
                  Counter 1: {counter}
                  <button
                    onClick={handleBtnClick}
                    style={{
                      display: "inline",
                      marginLeft: "20px",
                    }}
                  >
                    Increment
                  </button>
                </div>
                <div>
                  <h5
                    className="blue-color"
                    style={{ marginTop: "20px", marginBottom: "0px" }}
                  >
                    <div>useState with a function parameter: </div>
                    <div>{"useState(() => { return 0; })"}</div>
                  </h5>
                </div>
                <div style={{ marginTop: "0px" }}>
                  Counter 2: {counter2}
                  <button
                    onClick={handleBtn2Click}
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
          
          export default ComponentUseState;
          
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    - Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import ComponentUseState from "./ComponentUseState";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>React Hook: useState</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>useState</h3>
                      <div>
                        <ComponentUseState />
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
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usestate/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usestate/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usestate/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usestate/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-hooks-usestate/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-hooks-usestate
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usestate/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-hooks-usestate.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Hooks - useState
           
           :custom-color-primary-bold:`React Hooks - useState`
           
