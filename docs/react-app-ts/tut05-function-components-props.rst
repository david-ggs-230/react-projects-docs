.. _tut05-function-components-props:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Function Components - Props
##################################################################################################

In React, props (short for "properties") are used to pass data from a parent component to a child component. In function components, props are simply passed as arguments to the function. Props allow components to be dynamic and reusable by passing different values to the same component. Props are read-only, meaning that a component cannot modify its own props directly. They are used to configure and customize the behavior and display of a component.
    
    - Props are passed down from the parent: A parent component can pass data to a child component through props as attributes.
    - Props are immutable: In the child component, props cannot be modified. They are treated as read-only data.
    - Accessing props: Props are passed as an argument to the function. Props can be accessed either directly or by using destructuring to extract specific values.
    - Default props can be defined to ensure a value is available even when not passed by the parent. This ensures that the component still behaves as expected even if no value is passed for a prop.
    
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-props --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-props> ::
        
        cd tut05-function-components-props
        
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
            max-width: 600px;
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
Create Function Components Using Props
**************************************************************************************************

==================================================================================================
Creating TypeScript object types
==================================================================================================
    
    - TypeScript enhances JavaScript by providing a comprehensive type system, and its type checking can detect errors at an early stage.
    - A TypeScript Person object is created to store a person's properties, such as name, age, and location. Its type structure is defined as follows: 
        
        .. code-block:: tsx
          :caption: src/Person.tsx
          :linenos:
          
          import React from "react";
          
          type Person = {
            name?: string;
            age?: number;
            location?: string;
            label?: string;
            children?: React.ReactNode;
            propAccess?: "destructuring" | "default";
          };
          
          export default Person;
          
==================================================================================================
Passing and Accessing Props
==================================================================================================

In React, passing and accessing props in a function component is simple and straightforward:
    
    - Passing Props to a Function Component (Passing props from a parent component to a child component)
        
        - The props are passed as attributes in the JSX, and the child component can access them.
        - The destructuring props are passed as attributes in the JSX, and the child component can access them.
        - If a prop is not passed, the child component will use default values.
        
    - Accessing Props to a Function Component (a child component access props passed from a parent component)
        
        - ChildComponent accesses the props object.
        - ChildComponent accesses the destructured props object
        
    
    - Create a child function Component accessing the props object.
        
        .. code-block:: tsx
          :caption: src/ChildComponentWithPropsArgs.tsx
          :linenos:
          
          import Person from "./Person";
          
          const ChildComponentWithPropsArgs: React.FC<Person> = (props: Person) => {
            const {
              name = "Unknown Name",
              age = NaN,
              location = "Unknown Location",
            } = { ...props };
            return (
              <>
                {/*<div>Name: {props.name ? props.name : "Unknown Name"}</div>*/}
                {/*<div>Age: {props.age ? props.age : "NaN"}</div>*/}
                {/*<div>
                  Location: {props.location ? props.location : "Unknown Location"}
                </div> */}
                <div>Name: {name}</div>
                <div>Age: {age}</div>
                <div>Location: {location}</div>
              </>
            );
          };
          
          export default ChildComponentWithPropsArgs;
          
    - Create a child function Component accessing the destructured props object
        
        .. code-block:: tsx
          :caption: src/ChildComponentWithDestrucingPropsArgs.tsx
          :linenos:
          
          import React from "react";
          import Person from "./Person";
          
          const ChildComponentWithDestrucingPropsArgs: React.FC<Person> = ({
            name = "Unknown Name",
            age = NaN,
            location = "Unknown Location",
          }) => {
            return (
              <>
                <div>Name: {name}</div>
                <div>Age: {age}</div>
                <div>Location: {location}</div>
              </>
            );
          };
          
          export default ChildComponentWithDestrucingPropsArgs;
          
    - Create a parent function Component passing props to its child component
        
        .. code-block:: cfg
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import React from "react";
          import ChildComponentWithDestrucingPropsArgs from "./ChildComponentWithDestrucingPropsArgs";
          import ChildComponentWithPropsArgs from "./ChildComponentWithPropsArgs";
          import Person from "./Person";
          import "./list-style.css";
          
          const FunctionComponentsDisplay: React.FC = () => {
            const person: Person = {
              name: "John Doe",
              age: 30,
              location: "New York",
            };
            return (
              <div className="list-container">
                <h2>Using Props in a React Function Component</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Parent: Passing props arguments</h3>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Child: Accessing arguments using props
                      </h5>
          
                      <div style={{ textAlign: "left", paddingLeft: "20px" }}>
                        &lt;ChildComponentWithPropsArgs <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;name=&quot;John Doe&quot; <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;age=&#123;30&#125; <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;location=&quot;New York&quot; <br />
                        /&gt;
                      </div>
          
                      <div>
                        <ChildComponentWithPropsArgs
                          name="John Doe"
                          age={30}
                          location="New York"
                        />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Parent: Passing destructuring props</h3>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Child: Accessing arguments using props
                      </h5>
          
                      <div style={{ textAlign: "left", paddingLeft: "20px" }}>
                        &lt;ChildComponentWithPropsArgs <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;&#123; ...person&#125; <br />
                        /&gt;
                      </div>
          
                      <div>
                        <ChildComponentWithPropsArgs {...person} />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Parent: Passing props arguments</h3>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Child: Accessing arguments using destrucing props
                      </h5>
          
                      <div style={{ textAlign: "left", paddingLeft: "20px" }}>
                        &lt;ChildComponentWithDestrucingPropsArgs <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;name=&quot;John Doe&quot; <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;age=&#123;30&#125; <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;location=&quot;New York&quot; <br />
                        /&gt;
                      </div>
          
                      <div>
                        <ChildComponentWithDestrucingPropsArgs
                          name="John Doe"
                          age={30}
                          location="New York"
                        />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Parent: Passing destructuring props</h3>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Child: Accessing arguments using destrucing props
                      </h5>
          
                      <div style={{ textAlign: "left", paddingLeft: "20px" }}>
                        &lt;ChildComponentWithDestrucingPropsArgs <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;&#123; ...person&#125; <br />
                        /&gt;
                      </div>
          
                      <div>
                        <ChildComponentWithDestrucingPropsArgs {...person} />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Parent: Passing no arguments</h3>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Child: Accessing default arguments using props
                      </h5>
          
                      <div style={{ textAlign: "left", paddingLeft: "20px" }}>
                        &lt;ChildComponentWithPropsArgs /&gt;
                      </div>
          
                      <div>
                        <ChildComponentWithPropsArgs />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Parent: Passing no arguments</h3>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Child: Accessing default arguments using destrucing props
                      </h5>
          
                      <div style={{ textAlign: "left", paddingLeft: "20px" }}>
                        &lt;ChildComponentWithDestrucingPropsArgs /&gt;
                      </div>
          
                      <div>
                        <ChildComponentWithDestrucingPropsArgs />
                      </div>
                    </div>
                  </li>
                </ol>
              </div>
            );
          };
          
          export default FunctionComponentsDisplay;
          
==================================================================================================
Render the component
==================================================================================================
    
    - Edit ``App.tsx`` to render the component
        
        .. code-block:: tsx
          :caption: src/App.tsx
          :linenos:
          
          import FunctionComponentsDisplay from "./FunctionComponentDisplay";
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
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-props/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-props/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-props/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-props/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-props/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-props
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-props/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-props.png
           :align: center
           :class: sd-my-2
           :width: 80%
           :alt: React Function Components - Props
           
           :custom-color-primary-bold:`React Function Components - Props`