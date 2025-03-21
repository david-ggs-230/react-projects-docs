.. _tut05-function-components-hooks-usecontext:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Hooks - useContext
##################################################################################################

useContext is used to access values from a React Context without needing to pass props manually at every level of the component tree. Context is one of the important concept in React. It provides the ability to pass a information from the parent component to all its children to any nested level without passing the information through props in each level. Context will make the code more readable and simple to understand. Context can be used to store information which does not change or have minimal change. Some of the use cases of context are as follows
    
    - Application configuration
    - Current authenticated user information
    - Current user setting
    - Language setting
    - Theme / Design configuration by application / users
    
Context usage through hook
    
    - Creating a new context ::
        
        // Create a context
        const ValueContext = React.createContext("default value");
        // Create a Context with Multiple Objects
        const ThemeContext = React.createContext({
           color: 'black',
           backgroundColor: 'white'
        })
        // Create a Context with Objects and functions
        const ThemeContext = React.createContext<ThemeType>({
          theme: { color: "black", backgroundColor: "white" },
          setTheme: () => {},
        });
        
        
    - Setting context provider in the root component ::
        
        <ThemeContext.Provider value={{
           color: 'white',
           backgroundColor: 'green'
        }}>
            <children components.../>
        </ThemeContext.Provider>
        
    - Setting context consumer in the component where we need the context information ::
        
        import ThemeContext from "ThemeContext";
        const theme = useContext(ThemContext)
        
    - Accessing context information and using it in render method ::
        
        let theme = useContext(ThemeContext)
        return (
           <div style={{
              color: theme.color,
              backgroundColor: theme.backgroundColor }}>
                 Hello World
           </div>
        )
        
Updating context: Updating the context will rerender all the child component. React provides an option to update the context by using both useState and useContext hook.
    
    - In the root component, use useState hook to manage the theme information ::
        
        const [theme, setTheme] = useState({...})
        <ThemeContext.Provider value={{ theme, setTheme }}>
            <children components.../>
        </ThemeContext.Provider>
        
    - In the component where we need the context information, use useContext and state update function ::
        
        import ThemeContext from "ThemeContext";
        let { theme, setTheme } = useContext(ThemeContext)
        const handleClick=(color)=>{
          setTheme({color: color});
        }
        
    

**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-hooks-usecontext --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-hooks-usecontext> ::
        
        cd tut05-function-components-hooks-usecontext
        
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
Component - useContext
**************************************************************************************************

==================================================================================================
Function Components - the useContext Hook
==================================================================================================
    
    - Define a module to hold the context objects.
        
        .. code-block:: tsx
          :caption: src/CreateContextObjects.tsx
          :linenos:
          
          import React, { Dispatch, SetStateAction } from "react";
          
          // Create a context
          const ValueContext = React.createContext("default value");
          
          type ThemeType = {
            theme: { color: string; backgroundColor: string };
            setTheme: Dispatch<
              SetStateAction<{ color: string; backgroundColor: string }>
            >;
          };
          // Create a Context
          const ThemeContext = React.createContext<ThemeType>({
            theme: { color: "black", backgroundColor: "white" },
            setTheme: () => {},
          });
          export { ValueContext, ThemeContext };
          
    - Define a function component to use the context objects.
        
        .. code-block:: tsx
          :caption: src/ComponentUseContextValue.tsx
          :linenos:
          
          import { useContext } from "react";
          import { ValueContext } from "./CreateContextObjects";
          
          import "./list-style.css";
          
          const ComponentUseContextValue = () => {
            // Access context value
            const value = useContext(ValueContext);
            return (
              <>
                <h5
                  className="blue-color"
                  style={{ marginTop: "20px", marginBottom: "0px" }}
                >
                  <div>useContext with an initial value</div>
                </h5>
                <div style={{ marginTop: "0px" }}>
                  initial context value: <span className="red-color">{value}</span>
                </div>
              </>
            );
          };
          
          export default ComponentUseContextValue;
          
    - Define a function component to update the context objects.
        
        .. code-block:: tsx
          :caption: src/ComponentUpdateContextValue.tsx
          :linenos:
          
          import { useContext, useRef } from "react";
          import { ThemeContext } from "./CreateContextObjects";
          import "./list-style.css";
          
          const ComponentUpdateContextValue = () => {
            // Access context value
            const { theme, setTheme } = useContext(ThemeContext);
            const blueBtnBorderRef = useRef("white");
            const redBtnBorderRef = useRef("white");
            const handleClick = (color: string) => {
              if (color === "red") {
                redBtnBorderRef.current = "lightcoral";
                blueBtnBorderRef.current = "white";
              } else if (color === "blue") {
                blueBtnBorderRef.current = "lightblue";
                redBtnBorderRef.current = "white";
              }
              setTheme({ color: color, backgroundColor: color });
            };
            return (
              <>
                <h5
                  className="blue-color"
                  style={{ marginTop: "20px", marginBottom: "0px" }}
                >
                  <div>useContext with useState to update context value</div>
                </h5>
                <div style={{ marginTop: "0px" }}>
                  Context Color:{" "}
                  <span style={{ color: theme.color }}>{theme.color} </span>
                </div>
                <div style={{ marginTop: "0px" }}>
                  <button
                    style={{ backgroundColor: redBtnBorderRef.current }}
                    onClick={() => handleClick("red")}
                  >
                    Red
                  </button>
                  <button
                    style={{
                      marginLeft: "10px",
                      backgroundColor: blueBtnBorderRef.current,
                    }}
                    onClick={() => handleClick("blue")}
                  >
                    Blue
                  </button>
                </div>
              </>
            );
          };
          
          export default ComponentUpdateContextValue;
          
    - Define a function component with the useContext hook.
        
        .. code-block:: tsx
          :caption: src/ComponentuseContext.tsx
          :linenos:
          
          import { useState } from "react";
          import { ThemeContext, ValueContext } from "./CreateContextObjects";
          import ComponentUpdateContextValue from "./ComponentUpdateContextValue";
          import ComponentUseContextValue from "./ComponentUseContextValue";
          
          import "./list-style.css";
          
          const ComponentUseContext = () => {
            const [theme, setTheme] = useState({
              color: "green",
              backgroundColor: "lightgreen",
            });
          
            return (
              <>
                <ValueContext.Provider value="Hello, World!">
                  <ComponentUseContextValue />
                </ValueContext.Provider>
                <ThemeContext.Provider value={{ theme: theme, setTheme: setTheme }}>
                  <ComponentUpdateContextValue />
                </ThemeContext.Provider>
              </>
            );
          };
          
          export default ComponentUseContext;
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import ComponentUseContext from "./ComponentUseContext";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>React Hook: useContext</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>useState</h3>
                      <div>
                        <ComponentUseContext />
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
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usecontext/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usecontext/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usecontext/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usecontext/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-hooks-usecontext/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-hooks-usecontext
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-hooks-usecontext/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-hooks-usecontext.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Hooks - useContext
           
           :custom-color-primary-bold:`React Hooks - useContext`
           
