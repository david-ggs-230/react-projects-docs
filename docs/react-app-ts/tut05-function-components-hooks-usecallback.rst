.. _tut05-function-components-hooks-usecallback:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Hooks - useCallback
##################################################################################################

The useCallback hook is similar to useMemo hook and provides the functionality of memoizing the function instead of values. Since callback function in an integral part of the JavaScript programming and callback functions are passed by references, react provides a separate hook, useCallback to memoize the callback functions. The useCallback and useMemo Hooks are similar. The main difference is that useMemo returns a memoized value and useCallback returns a memoized function.

When to Use useCallback:
    
    - One reason to use useCallback is to prevent a component from re-rendering unless its props have changed.
    - Every time a component re-renders, its functions get recreated. When the function is passed to its child component as props, the props state has actually changed.
    - We can use the useCallback hook to prevent the function from being recreated unless necessary.
    
The signature of the useMemo hook is as follows ::
    
    const <memoized_callback_fn> = useCallback(<callback_fn>, <dependency_array>);
    # callback_fn − Callback function to be memorized.
    # dependency_array − Hold variables, upon which the callback function depends.
    # The output of the useCallback hook is the memoized callback function of the callback_fn.
    # The useCallback(callback_fn, dependency_array) is equivalent to useMemo(() => callback_fn, dependency_array).
    
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-hooks-usecallback --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-hooks-usecallback> ::
        
        cd tut05-function-components-hooks-usecallback
        
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
Component - useCallback
**************************************************************************************************

==================================================================================================
Function Components - the useCallback Hook
==================================================================================================
    
    - Define a child component for testing the useCallback hook.
        
        .. code-block:: tsx
          :caption: src/ComponentUseCallbackChild.tsx
          :linenos:
          
          import { useEffect, useRef, memo } from "react";
          import "./list-style.css";
          
          const ComponentUseCallbackChild = memo(function ComponentUseCallbackChild({
            count,
            func,
          }: {
            count: number;
            func: (m: number) => number;
          }) {
            const messagesRef = useRef([] as string[]);
            // Declare state with the useState hook
            const renderRef = useRef<number>(0);
            useEffect(() => {
              // Effect function - equivalent to componentDidMount and componentDidUpdate
              const messages = messagesRef.current;
              messages.push("Component mounted");
              return () => {
                // Cleanup function - equivalent to componentWillUnmount
                messages.push("Component unmounted");
              };
            }, []);
            useEffect(() => {
              messagesRef.current.push(`Calling: func(${count})`);
              func(count);
            }, [count, func]);
            return (
              <>
                {messagesRef.current.push(`Calling render: ${renderRef.current++}`) > 0
                  ? ""
                  : ""}
                <div style={{ marginTop: "10px" }}>
                  Counter:<span className="red-color"> {count} </span>
                </div>
                <h4>Child Log Messages:</h4>
                <ol>
                  {messagesRef.current.map((message, index) => (
                    <li key={index} className="list-item" style={{ margin: "1px" }}>
                      <div>
                        {index + 1}. {message}
                      </div>
                    </li>
                  ))}
                </ol>
              </>
            );
          });
          
          export default ComponentUseCallbackChild;
          
    - Define a function component with the useCallback hook.
        
        .. code-block:: tsx
          :caption: src/ComponentUseCallback.tsx
          :linenos:
          
          import { useState, useRef, useCallback } from "react";
          import ComponentUseCallbackChild from "./ComponentUseCallbackChild";
          import "./list-style.css";
          
          const ComponentUseCallback = () => {
            const messagesRef = useRef([] as string[]);
            // Declare state with the useState hook
            const [counter, setCounter] = useState(10);
            const [rerender, setRerender] = useState(true);
            const renderRef = useRef<number>(0);
          
            const handleCountChange = () => {
              messagesRef.current.push(`Button Click: Counter++`);
              setCounter(counter + 1);
            };
            const handleRerender = () => {
              messagesRef.current.push(`Button Click: Re-Render`);
              setRerender(!rerender);
            };
            const func1 = useCallback(
              (num: number): number => {
                messagesRef.current.push(`Calling: func1(${counter})`);
                return num + 3;
              },
              [counter],
            );
            const func2 = (num: number): number => {
              messagesRef.current.push(`Calling: func1(${num})`);
              return num + 3;
            };
            return (
              <>
                {messagesRef.current.push(`Calling render: ${renderRef.current++}`) > 0
                  ? ""
                  : ""}
                <div>
                  <h5
                    className="blue-color"
                    style={{ marginTop: "20px", marginBottom: "0px" }}
                  >
                    <div>useCallback: Skipping re-rendering of child components</div>
                  </h5>
                  <div style={{ marginTop: "10px" }}>
                    Counter:<span className="red-color"> {counter} </span>
                  </div>
          
                  <div style={{ marginTop: "10px" }}>
                    <button onClick={handleCountChange}>Counter++</button>
                    <button
                      style={{
                        marginLeft: "10px",
                      }}
                      onClick={handleRerender}
                    >
                      Re-Render
                    </button>
                  </div>
                </div>
                <h4>Parent Log Messages:</h4>
                <ol>
                  {messagesRef.current.map((message, index) => (
                    <li key={index} className="list-item" style={{ margin: "1px" }}>
                      <div>
                        {index + 1}. {message}
                      </div>
                    </li>
                  ))}
                </ol>
                <div>
                  <h5
                    className="blue-color"
                    style={{ marginTop: "20px", marginBottom: "0px" }}
                  >
                    <div>With useCallback: Skipping re-rendering of child components</div>
                  </h5>
                </div>
                <ComponentUseCallbackChild count={counter} func={func1} />
                <div>
                  <h5
                    className="blue-color"
                    style={{ marginTop: "20px", marginBottom: "0px" }}
                  >
                    <div>Without useCallback: Re-rendering of child components</div>
                  </h5>
                </div>
                <ComponentUseCallbackChild count={counter} func={func2} />
              </>
            );
          };
          
          export default ComponentUseCallback;
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    - Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import ComponentUseCallback from "./ComponentUseCallback";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>React Hook: useCallback</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>useCallback</h3>
                      <div>
                        <ComponentUseCallback />
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
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usecallback/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usecallback/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usecallback/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usecallback/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-hooks-usecallback/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-hooks-usecallback
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usecallback/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-hooks-usecallback.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Hooks - useCallback
           
           :custom-color-primary-bold:`React Hooks - useCallback`
           
