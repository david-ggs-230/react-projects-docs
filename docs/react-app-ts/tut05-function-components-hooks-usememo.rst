.. _tut05-function-components-hooks-usememo:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Hooks - useMemo
##################################################################################################

The useMemo hook in React is used to optimize performance by memoizing (caching) the result of a computation or function call, preventing unnecessary recalculations on re-renders. This is especially useful when the computation is expensive or the result is likely to stay the same across renders.

When to Use useMemo:
    
    - When you have a computationally expensive function that depends on certain props or state values, and you want to avoid recalculating it on every render.
    - When passing down functions to child components, and you want to prevent re-renders of child components when certain props don’t change.
    
Using useMemo to Optimize a computationally expensive functions:
    
    - useMemo with Arguments: Use useMemo to memoize computations that take arguments, and only recompute the result when the arguments change.
    - The dependencies array determines when the memoized value should be recalculated. If any dependency changes, the function inside useMemo will be re-run to calculate the new result.
    - useMemo is particularly useful for avoiding unnecessary re-executions of expensive calculations in functional components.
    - Arguments are passed as state variables
    
Preventing Re-rendering of Expensive Child Component
    
    - useMemo is often used to optimize the rendering of child components by memoizing the props that are passed to them, especially when those props are computationally expensive to calculate.
    - ChildComponent won’t re-render unless props or states change to prevent unnecessary recalculations during every render of ParentComponent.
    - Arguments are passed using props
    
The signature of the useMemo hook is as follows ::
    
    const <output of the expensive logic> = useMemo(<expensive_fn>, <dependency_array>);
    const MemoizedComponent = React.memo(FunctionalComponent);
    # expensive_fn − Do the expensive logic and returns the output to be memoized.
    # dependency_array − Hold variables, upon which the expensive logic depends. If the value of the array changes,
    #    then the expensive logic has to be rerun and the value have to be updated.
    
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-hooks-usememo --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-hooks-usememo> ::
        
        cd tut05-function-components-hooks-usememo
        
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
Component - useMemo
**************************************************************************************************

==================================================================================================
Function Components - the useMemo Hook
==================================================================================================
    
    - Define a function component to use the useMemo hook.
        
        .. code-block:: tsx
          :caption: src/ComponentWithUseMemo.tsx
          :linenos:
          
          import { useState, useMemo, useRef } from "react";
          import "./list-style.css";
          
          const ComponentWithUseMemo = () => {
            const messagesRef = useRef([] as string[]);
            // Declare state with the useState hook
            const [counter, setCounter] = useState(10);
            const [rerender, setRerender] = useState(true);
            const renderRef = useRef<number>(0);
            const func = (num: number): number => {
              messagesRef.current.push(`Calculate: F(${num})`);
              return num + 3;
            };
          
            // Memoized function calculation
            const funcResult = useMemo(() => func(counter), [counter]);
            const handleCountChange = () => {
              messagesRef.current.push(`Button Click: Counter++`);
              setCounter(counter + 1);
            };
            const handleRerender = () => {
              messagesRef.current.push(`Button Click: Re-Render`);
              setRerender(!rerender);
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
                    <div>useMemo: Calling function with useMemo</div>
                  </h5>
                  <div style={{ marginTop: "10px" }}>
                    Counter:<span className="red-color"> {counter} </span>
                  </div>
                  <div
                    style={{ marginTop: "0px", marginLeft: "20px", textAlign: "left" }}
                  >
                    <div>
                      {messagesRef.current.push(`Get result: F(${counter})`) > 0
                        ? ""
                        : ""}
                      {`Get result: F(${counter}) = `}
                      <span className="red-color">{funcResult}</span>
                    </div>
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
                <h4>Log Messages:</h4>
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
          };
          
          export default ComponentWithUseMemo;
          
    - Define a function component not using the useMemo hook.
        
        .. code-block:: tsx
          :caption: src/ComponentWithOutUseMemo.tsx
          :linenos:
          
          import { useState, useRef } from "react";
          import "./list-style.css";
          
          const ComponentWithOutUseMemo = () => {
            const messagesRef = useRef([] as string[]);
            // Declare state with the useState hook
            const [counter, setCounter] = useState(10);
            const [rerender, setRerender] = useState(true);
            const renderRef = useRef<number>(0);
            const func = (num: number): number => {
              messagesRef.current.push(`Calculate: F(${num})`);
              return num + 3;
            };
          
            //const funcResult = useMemo(() => func(counter), [counter]);
            const funcResult = func(counter);
            const handleCountChange = () => {
              messagesRef.current.push(`Button Click: Counter++`);
              setCounter(counter + 1);
            };
            const handleRerender = () => {
              messagesRef.current.push(`Button Click: Re-Render`);
              setRerender(!rerender);
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
                    <div>useMemo: Calling function without useMemo</div>
                  </h5>
                  <div style={{ marginTop: "10px" }}>
                    Counter:<span className="red-color"> {counter} </span>
                  </div>
                  <div
                    style={{ marginTop: "0px", marginLeft: "20px", textAlign: "left" }}
                  >
                    <div>
                      {messagesRef.current.push(`Get result: F(${counter})`) > 0
                        ? ""
                        : ""}
                      {`Get result: F(${counter}) = `}
                      <span className="red-color">{funcResult}</span>
                    </div>
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
                <h4>Log Messages:</h4>
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
          };
          
          export default ComponentWithOutUseMemo;
          
    - Define a function component using the React.memo
        
        .. code-block:: tsx
          :caption: src/ComponentReactMemoChild.tsx
          :linenos:
          
          import { useEffect, useRef, memo } from "react";
          import "./list-style.css";
          
          const ComponentReactMemoChild = memo(function ComponentReactMemoChild({
            count,
          }: {
            count: number;
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
                    <div>With React.memo: Skipping re-rendering of child components</div>
                  </h5>
                  <div style={{ marginTop: "10px" }}>
                    Counter:<span className="red-color"> {count} </span>
                  </div>
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
          
          export default ComponentReactMemoChild;
          
    - Define a function component not using the React.memo
        
        .. code-block:: tsx
          :caption: src/ComponentReactMemoNotOnChild.tsx
          :linenos:
          
          import { useEffect, useRef } from "react";
          import "./list-style.css";
          
          function ComponentReactMemoNotOnChild({ count }: { count: number }) {
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
                    <div>Without React.memo: Re-rendering of child components</div>
                  </h5>
                  <div style={{ marginTop: "10px" }}>
                    Counter:<span className="red-color"> {count} </span>
                  </div>
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
          }
          
          export default ComponentReactMemoNotOnChild;
          
    - Define a function component showing the using or not using React.memo.
        
        .. code-block:: tsx
          :caption: src/ComponentReactMemo.tsx
          :linenos:
          
          import { useState, useRef } from "react";
          import ComponentReactMemoChild from "./ComponentReactMemoChild";
          import ComponentReactMemoNotOnChild from "./ComponentReactMemoNotOnChild";
          import "./list-style.css";
          
          const ComponentReactMemo = () => {
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
                    <div>React.memo: Skipping re-rendering of child components</div>
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
                <ComponentReactMemoChild count={counter} />
                <ComponentReactMemoNotOnChild count={counter} />
              </>
            );
          };
          
          export default ComponentReactMemo;
          
    - Define a function component showing the using or not using useMemo hooks.
        
        .. code-block:: tsx
          :caption: src/ComponentUseMemo.tsx
          :linenos:
          
          import ComponentReactMemo from "./ComponentReactMemo";
          import ComponentWithOutUseMemo from "./ComponentWithOutUseMemo";
          import ComponentWithUseMemo from "./ComponentWithUseMemo";
          import "./list-style.css";
          
          const ComponentUseMemo = () => {
            return (
              <>
                <ComponentWithUseMemo />
                <ComponentWithOutUseMemo />
                <ComponentReactMemo />
              </>
            );
          };
          
          export default ComponentUseMemo;
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    - Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import ComponentUseMemo from "./ComponentUseMemo";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>React Hook: useMemo</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>useMemo</h3>
                      <div>
                        <ComponentUseMemo />
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
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usememo/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usememo/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usememo/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usememo/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-hooks-usememo/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-hooks-usememo
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usememo/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-hooks-usememo.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Hooks - useMemo
           
           :custom-color-primary-bold:`React Hooks - useMemo`
           
