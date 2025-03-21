.. _tut05-function-components-hooks-useref:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Hooks - useRef
##################################################################################################

The useRef hook in React is commonly used for accessing and interacting with DOM elements or for storing mutable values that do not trigger a re-render when they change. The useRef hook helps ensure that the component works smoothly with both React’s Virtual DOM and the HTML DOM. 
    
    - Accessing DOM Elements: You can use useRef to directly reference a DOM element and interact with it (e.g., focusing an input field).
    - Storing Mutable Values: You can use useRef to store values that persist across renders, but changes to those values do not cause re-renders.
    
How useRef Works with Virtual DOM and HTML DOM
    
    - Persistent Reference: using useRef allows you to interact with the real HTML DOM directly without causing a re-render or needing to store the value in React state.
    - No Re-rendering on Changes: Unlike state (useState), updating the current property of a useRef does not cause the component to re-render. 
    
The signature of useRef is as follows ::
    
    <refObj> = useRef(<val>)
    # val is the initial value to be set for the returned mutable object, refObj.
    # refObj is the object returned by the hook.
    
To automatically attach a DOM object to the refObj, it should be set in ref props of the element as shown below ::
    
    <input ref={refObj} />
    
To access the attached DOM element, use current property of the refObj as shown below ::
    
    const refElement = refObj.current
    
Use cases of useRef
    
    - Accessing JavaScript DOM API
        
        - Focusing an input element
        - Selecting text
        - play audio or video using media playback API
        
    - Imperative animation − Web Animation API provides a rich set of animation feature through imperative programming rather than declarative programming. To use Web animation API, we need access to the raw DOM.
    - Integration with third party library − Since third party library requires access to raw DOM to do its functionality, it is be mandatory to use useRef to get the DOM reference from react and provide it to third party library.
    
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-hooks-useref --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-hooks-useref> ::
        
        cd tut05-function-components-hooks-useref
        
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
Component - useRef
**************************************************************************************************

==================================================================================================
Function Components - the useRef Hook
==================================================================================================
    
    - Define a function component to use the useRef hook.
        
        .. code-block:: tsx
          :caption: src/ComponentUseRef.tsx
          :linenos:
          
          import "./list-style.css";
          import { useState, useRef } from "react";
          
          const ComponentUseRef = () => {
            const inputRef = useRef<HTMLInputElement>(null);
            const labelRef = useRef<HTMLLabelElement>(null);
            const handleInputChange = () => {
              if (labelRef.current && inputRef.current) {
                labelRef.current.innerText = inputRef.current.value;
              }
            };
          
            const [seconds, setSeconds] = useState(0);
            const timerRef = useRef<number>(NaN);
            const startTimer = () => {
              if (!isNaN(timerRef.current)) return; // Don't start a new timer if one is already running
          
              timerRef.current = setInterval(() => {
                setSeconds((prev) => prev + 1);
              }, 1000);
            };
          
            const stopTimer = () => {
              if (timerRef.current) {
                // Clear the timer if it exists
                clearInterval(timerRef.current);
              }
              // Reset the timerRef to NaN
              timerRef.current = NaN;
            };
            const prevCountRef = useRef(-1);
            const [count, setCount] = useState(0);
          
            const handleCountChange = () => {
              setCount((prev) => {
                prevCountRef.current = prev;
                return prev + 1;
              });
            };
          
            return (
              <>
                <div>
                  <h5
                    className="blue-color"
                    style={{ marginTop: "20px", marginBottom: "0px" }}
                  >
                    <div>useRef: Accessing real DOM Elements directly</div>
                  </h5>
                  <div style={{ marginTop: "0px" }}>
                    <input
                      ref={inputRef}
                      type="text"
                      placeholder="Enter input field data"
                      onChange={handleInputChange}
                    />
                  </div>
                  <div style={{ marginTop: "10px" }}>
                    Input Value in HTML DOM:{" "}
                    <span style={{ color: "red" }} ref={labelRef} />
                  </div>
                </div>
                <div>
                  <h5
                    className="blue-color"
                    style={{ marginTop: "20px", marginBottom: "0px" }}
                  >
                    <div>useRef: Persisting Values Across Renders</div>
                  </h5>
                  <div style={{ marginTop: "0px" }}>
                    Timer:<span className="red-color"> {seconds} </span> seconds
                  </div>
                  <div style={{ marginTop: "0px" }}>
                    <button onClick={startTimer}>Start</button>
                    <button
                      style={{
                        marginLeft: "10px",
                      }}
                      onClick={stopTimer}
                    >
                      Stop
                    </button>
                  </div>
                </div>
                <div>
                  <h5
                    className="blue-color"
                    style={{ marginTop: "20px", marginBottom: "0px" }}
                  >
                    <div>useRef: Storing Previous State</div>
                  </h5>
                  <div style={{ marginTop: "0px" }}>Current count: {count}</div>{" "}
                  <div style={{ marginTop: "0px" }}>
                    Previous count:{" "}
                    {prevCountRef.current < 0 ? "N/A" : prevCountRef.current}
                  </div>
                  <div style={{ marginTop: "0px" }}>
                    <button onClick={handleCountChange}>Increment</button>
                  </div>
                </div>
              </>
            );
          };
          
          export default ComponentUseRef;
          
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import ComponentUseRef from "./ComponentUseRef";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>React Hook: useRef</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>useRef</h3>
                      <div>
                        <ComponentUseRef />
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
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-hooks-useref/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-hooks-useref/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-useref/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-useref/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-hooks-useref/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-hooks-useref
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-useref/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-hooks-useref.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Hooks - useRef
           
           :custom-color-primary-bold:`React Hooks - useRef`
           
