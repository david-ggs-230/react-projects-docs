.. _tut05-function-components-hooks-usereducer:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Hooks - useReducer
##################################################################################################

The useReducer hook in React is a powerful alternative to useState for managing complex state logic. It is often used when the state updates depend on previous states or involve multiple sub-values. Essentially, it allows you to handle state transitions in a more structured way, similar to how Redux works, but at the component level.

The useReducer hook is particularly useful when:
    
    - The state logic is complex (e.g., multiple state variables or conditionally updating state).
    - You need to manage actions (e.g., incrementing, decrementing, resetting a value) in a predictable way.
    - You want to keep state logic separate from the component logic.
    

The useReducer hook accepts a reducer function along with the initial value and returns a dispatcher function. Reducer function will accept the initial state and an action (specific scenario) and then provides logic to update the state based on the action. The dispatcher function accepts the action (and corresponding details) and call the reducer function with provided action. ::
    
    const [<state>, <dispatch function>] = useReducer(<reducer function>, <initial argument>, <init function>);
    # const [state, dispatch] = useReducer(reducer, initialState);
    #     reducer: A function that takes the current state and an action as arguments and returns the new state.
    #     initialState: The initial state for the reducer.
    #     state: The information to be maintained in the state
    
    
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-hooks-usereducer --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-hooks-usereducer> ::
        
        cd tut05-function-components-hooks-usereducer
        
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
Component - useReducer
**************************************************************************************************

==================================================================================================
Function Components - the useReducer Hook
==================================================================================================
    
    - Define a function component to use the useReducer hook.
        
        .. code-block:: tsx
          :caption: src/ComponentUseReducer.tsx
          :linenos:
          
          import "./list-style.css";
          import { useReducer } from "react";
          
          const ComponentUseReducer = () => {
            const initialState = { count: 0, color: "black" };
            const reducer = (
              state: { count: number; color: string },
              action: { type: string },
            ) => {
              switch (action.type) {
                case "increment":
                  return { ...state, count: state.count + 1, color: "red" };
                case "decrement":
                  return { ...state, count: state.count - 1, color: "green" };
                case "reset":
                  return { ...state, count: 0, color: "blue" };
                default:
                  return state;
              }
            };
            const [state, dispatch] = useReducer(reducer, initialState);
          
            const handleClick = (type: { type: string }) => {
              dispatch(type);
            };
          
            return (
              <>
                <div>
                  <h5
                    className="blue-color"
                    style={{ marginTop: "20px", marginBottom: "0px" }}
                  >
                    <div>useReducer: handle more complex state updates and logic</div>
                  </h5>
                  <div style={{ marginTop: "0px" }}>
                    Count:{" "}
                    <span style={{ color: state.color, fontWeight: "bold" }}>
                      {state.count}
                    </span>
                  </div>
                  <div style={{ marginTop: "10px" }}>
                    <button onClick={() => handleClick({ type: "increment" })}>
                      Increment
                    </button>
                    <button
                      style={{ marginLeft: "10px" }}
                      onClick={() => handleClick({ type: "decrement" })}
                    >
                      Decrement
                    </button>
                    <button
                      style={{ marginLeft: "10px" }}
                      onClick={() => handleClick({ type: "reset" })}
                    >
                      Reset
                    </button>
                  </div>
                </div>
              </>
            );
          };
          
          export default ComponentUseReducer;
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import ComponentUseReducer from "./ComponentUseReducer";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>React Hook: useReducer</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>useReducer</h3>
                      <div>
                        <ComponentUseReducer />
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
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usereducer/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usereducer/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usereducer/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usereducer/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-hooks-usereducer/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-hooks-usereducer
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usereducer/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-hooks-usereducer.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Hooks - useReducer
           
           :custom-color-primary-bold:`React Hooks - useReducer`
           
