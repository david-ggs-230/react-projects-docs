.. _tut05-function-components-hooks:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Function Components - Hooks
##################################################################################################

React Hooks are functions that let you **"hook into"** React state and lifecycle features from function components. Hooks were added to React in version 16.8. React hooks are a powerful feature that allow you to use state, lifecycle methods, and other React features in functional components. 

React Hooks are powerful tools, but they come with certain rules to ensure that they work as expected. These rules must be followed to avoid unexpected behavior in your components. Here are the core rules for using React Hooks:
    
    -  Only Call Hooks at the Top Level
        
        Hooks must be called at the top level of your component or custom hook. They cannot be called conditionally or inside loops or nested functions. This ensures that hooks are always called in the same order on every render. Calling hooks conditionally or inside loops could result in them being invoked in a different order on different renders, leading to bugs and unpredictable behavior.
        
    - Only Call Hooks from React Functions
        
        You can only call hooks from React function components or custom hooks. You cannot use hooks in regular JavaScript functions or class components. Hooks rely on the React rendering lifecycle. Using hooks outside of React components means React can’t keep track of them properly.
        
    - Use Hooks in Custom Hooks
        
        If you are building custom hooks, you can call other hooks within them, but they must still follow the same rules: hooks must be called at the top level and only inside function components or other custom hooks. Custom hooks must still follow the rules of hooks. Calling hooks conditionally or in loops will break React’s rules and lead to unpredictable results.
        
    - Hooks Must Be Called in the Same Order
        
        Each hook call must be executed in the same order every time the component renders. This means you cannot call hooks based on conditions, such as inside if statements or loops. React needs to track the order in which hooks are called, so skipping or reordering hooks can break React’s internal state tracking.
        
    - Calling hooks conditionally
        
        If you need conditional logic, you can use hooks, but make sure the hooks themselves are not called conditionally. You can use conditionals inside the hook function.
        
    - Custom Hook names
        
        By convention, custom hook names should start with use (e.g., useCounter, useFetch), which ensures that React can enforce the rules of hooks.
        
        
The main hooks include useState, useEffect, useContext, useReducer, useCallback, useMemo, useRef, and useImperativeHandle, among others. These hooks provide ways to access React features, allowing you to better organize and reuse your code.

**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-hooks --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-hooks> ::
        
        cd tut05-function-components-hooks
        
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
React Hooks
**************************************************************************************************

==================================================================================================
useState
==================================================================================================

--------------------------------------------------------------------------------------------------
The signature of the useState
--------------------------------------------------------------------------------------------------

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
    
--------------------------------------------------------------------------------------------------
Component - useState
--------------------------------------------------------------------------------------------------

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
useEffect
==================================================================================================

--------------------------------------------------------------------------------------------------
The signature of the useEffect
--------------------------------------------------------------------------------------------------


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
    
    
--------------------------------------------------------------------------------------------------
Component - useEffect
--------------------------------------------------------------------------------------------------

Define a function component with the useEffect hook.
        
        .. code-block:: tsx
          :caption: src/ComponentUseEffect.tsx
          :linenos:
          
          import { useState, useEffect } from "react";
          import "./list-style.css";
          
          const messages: string[] = [] as string[];
          const ComponentUseEffect = () => {
            // Declare state with the useState hook
            const [counter, setCounter] = useState(0);
          
            // Increment function
            const handleBtnClick = () => {
              setCounter((prevState) => prevState + 1);
              messages.push("Button was Clicked! Count is " + (counter + 1) + ".");
            };
          
            useEffect(() => {
              // Effect function - equivalent to componentDidMount and componentDidUpdate
              messages.push("Component mounted");
              return () => {
                // Cleanup function - equivalent to componentWillUnmount
                messages.push("Component unmounted");
              };
            }, []); // Empty dependency array to run only once on initial render
            useEffect(() => {
              // This will run after the component mounts and every time `count` changes
              messages.push("Component mounted or updated");
              // Cleanup function - equivalent to componentWillUnmount
              return () => {
                // Cleanup function - equivalent to componentWillUnmount
                messages.push("Component unmounted for [counter] <dependency>");
              };
            }, [counter]); // The effect depends on the `count` state
            return (
              <>
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
                  {messages.map((message, index) => (
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
useContext
==================================================================================================

useContext is used to access values from a React Context without needing to pass props manually at every level of the component tree.

--------------------------------------------------------------------------------------------------
The signature of the useContext
--------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------
Example
--------------------------------------------------------------------------------------------------

==================================================================================================
useRef
==================================================================================================

--------------------------------------------------------------------------------------------------
The signature of the useRef
--------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------
Example
--------------------------------------------------------------------------------------------------


==================================================================================================
useReducer
==================================================================================================

--------------------------------------------------------------------------------------------------
The signature of the useReducer
--------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------
Example
--------------------------------------------------------------------------------------------------



==================================================================================================
useMemo
==================================================================================================

--------------------------------------------------------------------------------------------------
The signature of the useMemo
--------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------
Example
--------------------------------------------------------------------------------------------------




==================================================================================================
useCallback
==================================================================================================

--------------------------------------------------------------------------------------------------
The signature of the useCallback
--------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------
Example
--------------------------------------------------------------------------------------------------





==================================================================================================
Custom Hooks
==================================================================================================

--------------------------------------------------------------------------------------------------
The signature of the Custom Hooks
--------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------
Example
--------------------------------------------------------------------------------------------------


**************************************************************************************************
Create a Function Component to Show the User Interface
**************************************************************************************************
    
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
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-hooks/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-hooks/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-hooks/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-hooks
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-hooks.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Function Components - Life Cycles
           
           :custom-color-primary-bold:`React Function Components - Life Cycles`