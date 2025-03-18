.. _tut05-function-components-hooks-useeffect:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Hooks - useEffect
##################################################################################################

React provides useEffect to do side-effects in a component. Some of the side effects are as follows ::
    
    - Fetching data from external source & updating the rendered content.
    - Updating DOM elements after rendering.
    - Subscriptions
    - Using Timers
    - Logging
    
In class based components, these side effects are done using life cycle components. So, useEffect hook is an effect replacement for below mentioned life cycle events. ::
    
    - componentDidMount − Fires after the rendering is done for the first time.
    - componentDidUpdate − Fires after the rendering is updated due to prop or state changes.
    - componentWillUnmount − Fires after the rendered content is unmounted during destruction of component.
    
The signature of useEffect is as follows ::
    
    useEffect( <update function>, <dependency> )
    # the signature of the update function is:
    #    {
    #       // code
    #       return <clean up function>
    #    }
    
useEffect( <update function>, <dependency> ):
    
    - Update function − Update function is the function to be executed after each render phase. This corresponds to componentDidMount and componentDidUpdate events
    - Dependency − Dependency is an array with all the variables on which the function is dependent. Specifying the dependency is very important to optimize the effect hook. In general, update function is called after each render. Sometimes it is not necessary to render update function on each render.
    

**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-hooks-useeffect --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-hooks-useeffect> ::
        
        cd tut05-function-components-hooks-useeffect
        
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
Component - useEffect
**************************************************************************************************

==================================================================================================
Function Components - the useEffect Hook
==================================================================================================

    
    Define a function component with the useEffect hook.
        
        .. code-block:: tsx
          :caption: src/ComponentuseEffect.tsx
          :linenos:
          
          import { useState, useEffect, useRef } from "react";
          import "./list-style.css";
          
          const ComponentUseEffect = () => {
            // Declare state with the useState hook
            const messages = useRef([] as string[]);
            const [counter, setCounter] = useState(0);
            // Increment function
            const handleBtnClick = () => {
              setCounter((prevState) => prevState + 1);
              messages.current.push(
                "Button was Clicked! Count is " + (counter + 1) + ".",
              );
            };
          
            useEffect(() => {
              // Effect function - equivalent to componentDidMount and componentDidUpdate
              const currentMessages = messages.current;
              messages.current.push("Component mounted for [] <dependency>");
              return () => {
                // Cleanup function - equivalent to componentWillUnmount
                currentMessages.push("Component unmounted for [] <dependency>");
              };
            }, []); // Empty dependency array to run only once on initial render
            useEffect(() => {
              // This will run after the component mounts and every time `count` changes
              const currentMessages = messages.current;
              messages.current.push(
                "Component mounted or updated for [counter] <dependency>",
              );
          
              // Cleanup function - equivalent to componentWillUnmount
              return () => {
                // Cleanup function - equivalent to componentWillUnmount
                currentMessages.push("Component unmounted for [counter] <dependency>");
              };
            }, [counter]); // The effect depends on the `count` state
            return (
              <>
                {messages.current.push("Component Render") > 0 ? "" : ""}
                <div>
                  <h5
                    className="blue-color"
                    style={{ marginTop: "20px", marginBottom: "0px" }}
                  >
                    <div style={{ textAlign: "left" }}>
                      <div>Two useEffect hooks:</div>
                      <div style={{ marginLeft: "20px" }}>
                        <div>{"1. useEffect with empty dependency array:"}</div>{" "}
                        <div style={{ marginLeft: "40px" }}>
                          {"useEffect(() => {...},[]);"}
                        </div>
                        <div>{"2. useEffect with [counter] dependency array:"}</div>{" "}
                        <div style={{ marginLeft: "40px" }}>
                          {"useEffect(() => {...},[counter]);"}
                        </div>
                      </div>
                    </div>
                  </h5>
                </div>
                <div style={{ marginTop: "20px" }}>
                  Counter: {counter}
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
                <h4>Log Messages:</h4>
                <ol>
                  {messages.current.map((message, index) => (
                    <li key={index} className="list-item" style={{ margin: "1px" }}>
                      <div>
                        {index + 1}. {message}
                      </div>
                    </li>
                  ))}
                </ol>
              </>
            );
          };
          
          export default ComponentUseEffect;
          
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import ComponentUseEffect from "./ComponentUseEffect";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>React Hook: useEffect</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>useState</h3>
                      <div>
                        <ComponentUseEffect />
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
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-hooks-useeffect/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-hooks-useeffect/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-useeffect/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-useeffect/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-hooks-useeffect/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-hooks-useeffect
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-useeffect/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-hooks-useeffect.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Hooks - useEffect
           
           :custom-color-primary-bold:`React Hooks - useEffect`
           
