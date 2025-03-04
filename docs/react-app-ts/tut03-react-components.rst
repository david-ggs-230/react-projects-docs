.. _tut03-react-components:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Tut03-React Components
##################################################################################################

There are two types of components in React: 
    
    - Function Components 
        
        - They are JavaScript functions that return JSX.
        - Stateless or Stateful: Can manage state using React Hooks.
        - Simpler Syntax: Ideal for small and reusable components.
        - Performance: Generally faster since they don’t require a ``this`` keyword.
        
    - Class Components
        
        - Class components are ES6 classes that extend React.Component. 
        - Include features like state management and lifecycle methods.
            
            - State Management: State is managed using the this.state property.
            - Lifecycle Methods: Includes methods like componentDidMount, componentDidUpdate, etc.
            
            
**************************************************************************************************
Create a React Components Project
**************************************************************************************************

==================================================================================================
Create a React Project with Vite
==================================================================================================

--------------------------------------------------------------------------------------------------
Create a React Project
--------------------------------------------------------------------------------------------------
    
    - Create a ReactJS Project ::
        
        yarn create vite tut03-react-components --template react-ts
        
    - Move inside the ReactJS project folder <tut03-react-components> ::
        
        cd tut03-react-components
        
    - Install the dependencies ::
        
        yarn install
        
--------------------------------------------------------------------------------------------------
ESLint and Prettier Configuration
--------------------------------------------------------------------------------------------------
    
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
        
        yarn add --dev prettier eslint-plugin-prettier eslint-config-prettier  eslint-plugin-react 
        
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
            "lint": "eslint src --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
            "lint:fix": "eslint src --ext ts,tsx --fix",
          },
          
    - Run ESLint:
        
        .. code-block:: sh
          :linenos:
          
          yarn lint
          yarn lint:fix
          
        
--------------------------------------------------------------------------------------------------
Create Project CSS Styles
--------------------------------------------------------------------------------------------------
    
    Create the src/list-styles.css file with the following contents: 
        
        .. code-block:: css
          :caption: src/list-styles.css
          :linenos:
          
          
          .tree ul {
            padding-top: 20px;
            position: relative;
            transition: all 0.5s;
          }
          
          .tree li {
            float: left;
            text-align: center;
            list-style-type: none;
            position: relative;
            padding: 20px 5px 0 5px;
            transition: all 0.5s;
          }
          
          .tree li::before, .tree li::after {
            content: '';
            position: absolute;
            top: 0;
            right: 50%;
            border-top: 1px solid #ccc;
            width: 50%;
            height: 20px;
          }
          
          .tree li::after {
            right: auto;
            left: 50%;
            border-left: 1px solid #ccc;
          }
          
          .tree li:only-child::after, .tree li:only-child::before {
            display: none;
          }
          
          .tree li:only-child {
            padding-top: 0;
          }
          
          .tree li:first-child::before, .tree li:last-child::after {
            border: 0 none;
          }
          
          .tree li:last-child::before {
            border-right: 1px solid #ccc;
            border-radius: 0 5px 0 0;
          }
          
          .tree li:first-child::after {
            border-radius: 5px 0 0 0;
          }
          
          .tree ul ul::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            border-left: 1px solid #ccc;
            width: 0;
            height: 20px;
          }
          
          .tree li a {
            border: 1px solid #ccc;
            padding: 5px 10px;
            text-decoration: none;
            color: #666;
            font-family: arial, verdana, tahoma;
            font-size: 11px;
            display: inline-block;
            border-radius: 5px;
            transition: all 0.5s;
          }
          
          .tree li a:hover, .tree li a:hover+ul li a {
            background: #c8e4f8;
            color: #000;
            border: 1px solid #94a0b4;
          }
          
          .tree li a:hover+ul li::after,
          .tree li a:hover+ul li::before,
          .tree li a:hover+ul::before,
          .tree li a:hover+ul ul::before {
            border-color:  #94a0b4;
          }
        
--------------------------------------------------------------------------------------------------
Creating TypeScript object types
--------------------------------------------------------------------------------------------------
    
    - TypeScript enhances JavaScript by providing a comprehensive type system, and its type checking can detect errors at an early stage.
    - A TypeScript Person object is created to store a person's properties, such as name, age, and location. Its type structure is defined as follows: 
        
        .. code-block:: tsx
          :caption: src/Person.tsx
          :linenos:
          
          import React from "react";
          
          type Person = {
            name: string;
            age: number;
            location: string;
            label: string;
            children?: React.ReactNode;
          };
          
          export default Person;
          
==================================================================================================
Create React Function Components
==================================================================================================

--------------------------------------------------------------------------------------------------
Create a Child Function Component
--------------------------------------------------------------------------------------------------
    
    - A React function component is a JavaScript/TypeScript function that returns JSX.
    - Define a function component that holds a person's properties as shown below: 
        
        .. code-block:: tsx
          :caption: src/FunctionComponentChild.tsx
          :linenos:
          
          import React from "react";
          import Person from "./Person";
          
          const FunctionComponentChild: React.FC<Person> = ({
            label,
            name,
            age,
            location,
          }) => {
            return (
              <li>
                <a>
                  <h3>{label}</h3>
                  <div>Name: {name}</div>
                  <div>Age: {age}</div>
                  <div>Location: {location}</div>
                </a>
              </li>
            );
          };
          
          export default FunctionComponentChild;
          
    - FunctionComponentChild is a function component that accepts a person's properties as its arguments.
    

--------------------------------------------------------------------------------------------------
Create a Parent Function Component
--------------------------------------------------------------------------------------------------

    
    - A React component can have other React components as its nested child, HTML elements as its child, or use the {children} placeholder to wrap its child elements.
    - Define a parent function component structure that holds its own properties, with {children} serving as a placeholder to wrap its child components: 
        
        .. code-block:: tsx
          :caption: src/FunctionComponentParent.tsx
          :linenos:
          
          import React from "react";
          import Person from "./Person";
          import FunctionComponentChild from "./FunctionComponentChild";
          
          const FunctionComponentParent: React.FC<Person> = ({
            label,
            name,
            age,
            location,
            children,
          }) => {
            return (
              <li style={{ marginTop: "2rem" }}>
                <a>
                  <h2>{label}</h2>
                  <div>Name: {name}</div>
                  <div>Age: {age}</div>
                  <div>Location: {location}</div>
                </a>
                <ul>
                  {children}
                </ul>
              </li>
            );
          };
          
          export default FunctionComponentParent;
          
    - Add nested components to a parent function component as its child components, as shown below:
        
        .. code-block:: tsx
          :caption: src/FunctionComponentParent.tsx
          :linenos:
          
          ...
            <ul>
              <FunctionComponentChild
                label={"Child 1: As Nested Component"}
                name={"John Smith"}
                age={26}
                location={"New York"}
              ></FunctionComponentChild>
              {children}
            </ul>
          ...
          
    - Add HTML elements to a parent function component as its child components, as shown below:
        
        .. code-block:: tsx
          :caption: src/FunctionComponentParent.tsx
          :linenos:
          
          ...
            <ul>
              <FunctionComponentChild ... ></FunctionComponentChild>
              <li>
                <a>
                  <h3>Child 2: As HTML Elements</h3>
                  <div>Name: David Smith</div>
                  <div>Age: 23</div>
                  <div>Location: New York</div>
                </a>
              </li>
              {children}
            </ul>
          ...
          
    - The fully implemented parent function component that includes its own properties, along with nested components, HTML child elements, and {children} elements, as shown below:
        
        .. code-block:: tsx
          :caption: src/FunctionComponentParent.tsx
          :linenos:
          
          import React from "react";
          import Person from "./Person";
          import FunctionComponentChild from "./FunctionComponentChild";
          
          const FunctionComponentParent: React.FC<Person> = ({
            label,
            name,
            age,
            location,
            children,
          }) => {
            return (
              <li style={{ marginTop: "2rem" }}>
                <a>
                  <h2>{label}</h2>
                  <div>Name: {name}</div>
                  <div>Age: {age}</div>
                  <div>Location: {location}</div>
                </a>
                <ul>
                  <FunctionComponentChild
                    label={"Child 1: As Nested Component"}
                    name={"John Smith"}
                    age={26}
                    location={"New York"}
                  ></FunctionComponentChild>
                  <li>
                    <a>
                      <h3>Child 2: As HTML Elements</h3>
                      <div>Name: David Smith</div>
                      <div>Age: 23</div>
                      <div>Location: New York</div>
                    </a>
                  </li>
                  {children}
                </ul>
              </li>
            );
          };
          
          export default FunctionComponentParent;
          
==================================================================================================
Create React Class Components
==================================================================================================

--------------------------------------------------------------------------------------------------
Create a Child Class Component
--------------------------------------------------------------------------------------------------
    
    - A React class component is a JavaScript/TypeScript class that extends React.Component and uses a render function to return JSX.
    - In a React class component, you can use ``this`` to access the component's properties (or state) and methods.
    - Define a class component that holds a person's properties as shown below: 
        
        .. code-block:: tsx
          :caption: src/ClassComponentChild.tsx
          :linenos:
          
          import React from "react";
          import Person from "./Person";
          
          class ClassComponentChild extends React.Component<Person> {
            render() {
              return (
                <li>
                  <a>
                    <h3>{this.props.label}</h3>
                    <div>Name: {this.props.name}</div>
                    <div>Age: {this.props.age}</div>
                    <div>Location: {this.props.location}</div>
                  </a>
                </li>
              );
            }
          }
          
          export default ClassComponentChild;
          
    - ClassComponentChild is a class component that accepts a person's properties as its constructor arguments.
    

--------------------------------------------------------------------------------------------------
Create a Parent Class Component
--------------------------------------------------------------------------------------------------

    
    - A React component can have other React components as its nested child, HTML elements as its child, or use the {children} placeholder to wrap its child elements.
    - Define a parent class component structure that holds its own properties, with {children} serving as a placeholder to wrap its child components: 
        
        .. code-block:: tsx
          :caption: src/ClassComponentParent.tsx
          :linenos:
          
          import React from "react";
          import Person from "./Person";
          import ClassComponentChild from "./ClassComponentChild";
          class ClassComponentParent extends React.Component<Person> {
            render() {
              return (
                <li style={{ marginTop: "2rem" }}>
                  <a>
                    <h2>{this.props.label}</h2>
                    <div>Name: {this.props.name}</div>
                    <div>Age: {this.props.age}</div>
                    <div>Location: {this.props.location}</div>
                  </a>
                  <ul>
                    {this.props.children}
                  </ul>
                </li>
              );
            }
          }
          
          export default ClassComponentParent;
          
    - Add nested components to a parent class component as its child components, as shown below:
        
        .. code-block:: tsx
          :caption: src/ClassComponentParent.tsx
          :linenos:
          
          ...
            <ul>
              <ClassComponentChild
                label={"Child 1: As Nested Component"}
                name={"John Smith"}
                age={26}
                location={"New York"}
              ></ClassComponentChild>
              {children}
            </ul>
          ...
          
    - Add HTML elements to a parent class component as its child components, as shown below:
        
        .. code-block:: tsx
          :caption: src/ClassComponentParent.tsx
          :linenos:
          
          ...
            <ul>
              <ClassComponentChild ... ></ClassComponentChild>
              <li>
                <a>
                  <h3>Child 2: As HTML Elements</h3>
                  <div>Name: David Smith</div>
                  <div>Age: 23</div>
                  <div>Location: New York</div>
                </a>
              </li>
              {children}
            </ul>
          ...
          
    - The fully implemented parent class component that includes its own properties, along with nested components, HTML child elements, and {children} elements, as shown below:
        
        .. code-block:: tsx
          :caption: src/ClassComponentParent.tsx
          :linenos:
          
          import React from "react";
          import Person from "./Person";
          import ClassComponentChild from "./ClassComponentChild";
          class ClassComponentParent extends React.Component<Person> {
            render() {
              return (
                <li style={{ marginTop: "2rem" }}>
                  <a>
                    <h2>{this.props.label}</h2>
                    <div>Name: {this.props.name}</div>
                    <div>Age: {this.props.age}</div>
                    <div>Location: {this.props.location}</div>
                  </a>
                  <ul>
                    <ClassComponentChild
                      label={"Child 1: As Nested Component"}
                      name={"John Smith"}
                      age={26}
                      location={"New York"}
                    ></ClassComponentChild>
                    <li>
                      <a>
                        <h3>Child 2: As HTML Elements</h3>
                        <div>Name: David Smith</div>
                        <div>Age: 23</div>
                        <div>Location: New York</div>
                      </a>
                    </li>
                    {this.props.children}
                  </ul>
                </li>
              );
            }
          }
          
          export default ClassComponentParent;
          
--------------------------------------------------------------------------------------------------
Create a Testing Component
--------------------------------------------------------------------------------------------------
    
    - Create a Testing Component to load function components, class components, and nested components to showcase them.
    - Modify the App.tsx to act as the main testing component as shown below:
        
        .. code-block:: tsx
          :caption: src/App.tsx
          :linenos:
          
          import "./App.css";
          import ClassComponentChild from "./ClassComponentChild";
          import ClassComponentParent from "./ClassComponentParent";
          import FunctionComponentChild from "./FunctionComponentChild";
          import FunctionComponentParent from "./FunctionComponentParent";
          import "./list-styles.css";
          
          function App() {
            return (
              <>
                <div className="tree-container" style={{ display: "block" }}>
                  <div className="tree">
                    <ul>
                      <FunctionComponentParent
                        label={"Function Component: Parent"}
                        name={"Jane Doe"}
                        age={48}
                        location={"New York"}
                      >
                        <FunctionComponentChild
                          label={"Child 3: As {children}"}
                          name={"Lisa Smith"}
                          age={18}
                          location={"Boston"}
                        ></FunctionComponentChild>
                      </FunctionComponentParent>
                    </ul>
                  </div>
          
                  <div className="tree">
                    <ul>
                      <ClassComponentParent
                        label={"Class Component: Parent"}
                        name={"Jane Doe"}
                        age={48}
                        location={"New York"}
                      >
                        <ClassComponentChild
                          label={"Child 3: As {children}"}
                          name={"Lisa Smith"}
                          age={18}
                          location={"Boston"}
                        ></ClassComponentChild>
                      </ClassComponentParent>
                    </ul>
                  </div>
                </div>
              </>
            );
          }
          
          export default App;
          
--------------------------------------------------------------------------------------------------
Run the development app
--------------------------------------------------------------------------------------------------
    
    - Run dev
        
        .. code-block:: sh
          :linenos:
          
          yarn dev
          
    - Build
        
        .. code-block:: sh
          :linenos:
          
          yarn build
          
==================================================================================================
Hosting the React App on GitHub Pages
==================================================================================================

--------------------------------------------------------------------------------------------------
Build the App
--------------------------------------------------------------------------------------------------
    
    - Configure the build base url:
        
        - open vite.config.js file
        - set base to ``/react-projects/react-projects-with-typescript/tut03-react-components/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: '/react-projects/react-projects-with-typescript/tut03-react-components/',
            })
            
    - Build the app ::
        
        yarn run build
        
--------------------------------------------------------------------------------------------------
Hosting the App 
--------------------------------------------------------------------------------------------------
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut03-react-components/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut03-react-components/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``/react-projects-with-typescript/tut03-react-components/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut03-react-components
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut03-react-components/
    - Screenshot
        
        .. figure:: images/tut03/tut03-react-components-homepage.png
           :align: center
           :class: sd-my-2
           :width: 100%
           :alt: React Components
           
           :custom-color-primary-bold:`React Components`