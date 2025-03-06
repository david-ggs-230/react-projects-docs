.. _tut04-class-components-state:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Class Components - State
##################################################################################################

In React class components, state is used to store and manage data that can change over time within the component. The state allows a component to keep track of information between renders and update the user interface (UI) when the state changes.

A React class component manages and exposes its state through the this.state property. React provides a unified API to handle state within a component, which is this.setState(). This method accepts either a JavaScript object or a function that returns a JavaScript object. When the state is updated, the component triggers a re-render to reflect the changes in the UI.
    
    - State vs Props in Class Components:
        
        - State is used for data that can change over time and is local to the component.
        - Props are used to pass data from parent components to child components and are immutable inside the child component.
        
    
    - Key Concepts of State in React Class Components:
        
        - State is local to the component: Each instance of a class component has its own state, and it is not shared with other components unless explicitly passed down as props.
        - State is mutable: Unlike props, the state of a component can be changed over time.
        - State changes trigger re-renders: When the state changes, React re-renders the component to reflect the updated state in the UI.
        
    - How to Use State in React Class Components:
        
        - Initialize State: Initialize the state in the constructor method by calling this.state and setting the initial values.
        - Access State: Use this.state to access the state properties.
        - Update State: Use this.setState() to update the state. This method ensures that React re-renders the component and applies the updated state.
        
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut04-class-components-state --template react-ts
        
    - Move inside the ReactJS project folder <tut04-class-components-state> ::
        
        cd tut04-class-components-state
        
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
Create Class Components Using State
**************************************************************************************************

To demonstrate the usage of state in React class components with a parent counter and a child counter, we will create two class components:
    
    - The parent component will hold the state for the counter, and it will pass that state to the child component as props. Parent Component (ParentCounter):
        
        - The parent has its own counter (parentCounter) managed via the state (this.state.parentCounter).
        - It has a method handleParentBtnClick to update the parent’s counter when the button is clicked.
        - The parent passes its counter to the child via props (parentCounter).
        
    - The child component can modify the counter via a method provided by the parent. Child Component (ChildCounter):
        
        - The child maintains its own counter (childCounter) in the state (this.state.childCounter).
        - The child can increment its counter independently of the parent's counter by clicking the button.
        - The child has a method passed down by the parent as a prop to update the parent’s counter when the button is clicked.
        - The child's counter is updated via its own state (this.setState()), while the parent's counter is passed down as a prop.
        
==================================================================================================
Create a Class Component with State Data
==================================================================================================
    
    Define a class component with a state counter and a method to increment the counter.
        
        .. code-block:: tsx
          :caption: src/ParentComponentNoChild.tsx
          :linenos:
          
          import React from "react";
          
          interface ParentComponentState {
            parentCounter: number;
          }
          
          class ParentComponentNoChild extends React.Component<
            object,
            ParentComponentState
          > {
            constructor(props: object) {
              super(props);
              this.state = {
                parentCounter: 0,
              };
            }
            handleParentBtnClick = () => {
              this.setState((prevState) => ({
                parentCounter: prevState.parentCounter + 1,
              }));
            };
          
            render() {
              return (
                <>
                  <div style={{ marginTop: "20px" }}>
                    Parent Counter: {this.state.parentCounter}
                    <button
                      onClick={this.handleParentBtnClick}
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
            }
          }
          
          export default ParentComponentNoChild;
          
==================================================================================================
Create a Class Component Passing State Data to Child
==================================================================================================
    
    Define a class component with a state counter and a method to increment the counter, and passing the state counter and method to its child.
        
        .. code-block:: cfg
          :caption: src/ParentComponentWithChild.tsx
          :linenos:
          
          import React from "react";
          import ChildComponent from "./ChildComponent";
          
          interface ParentComponentState {
            parentCounter: number;
          }
          
          class ParentComponentWithChild extends React.Component<
            object,
            ParentComponentState
          > {
            constructor(props: object) {
              super(props);
              this.state = {
                parentCounter: 0,
              };
            }
            handleParentBtnClick = () => {
              this.setState((prevState) => ({
                parentCounter: prevState.parentCounter + 1,
              }));
            };
          
            render() {
              return (
                <>
                  <div style={{ marginTop: "20px" }}>
                    Parent Counter in Parent: {this.state.parentCounter}
                    <button
                      onClick={this.handleParentBtnClick}
                      style={{
                        display: "inline",
                        marginLeft: "20px",
                      }}
                    >
                      In Parent: Parent ++
                    </button>
                  </div>
                  <ChildComponent
                    parentCounter={this.state.parentCounter}
                    handleClick={this.handleParentBtnClick}
                  />
                </>
              );
            }
          }
          
          export default ParentComponentWithChild;
          
          
==================================================================================================
Create a Class Component Receiving State Data from Parent
==================================================================================================
    
    Define a class component with a state counter and a method to increment the counter, and receiving the parent's state counter and method as props.
        
        .. code-block:: cfg
          :caption: src/ChildComponent.tsx
          :linenos:
          
          import React from "react";
          
          interface ChildComponentProps {
            parentCounter: number;
            handleClick: () => void;
          }
          interface ChildComponentState {
            childCounter: number;
          }
          
          class ChildComponent extends React.Component<
            ChildComponentProps,
            ChildComponentState
          > {
            constructor(props: ChildComponentProps) {
              super(props);
              this.state = {
                childCounter: 0,
              };
            }
            handleChildBtnClick = () => {
              this.setState((prevState) => ({
                childCounter: prevState.childCounter + 1,
              }));
            };
          
            render() {
              return (
                <div style={{ marginTop: "20px" }}>
                  <div>Parent Counter in Child: {this.props.parentCounter}</div>
                  <div>Child Counter in Child: {this.state.childCounter}</div>
                  <div>
                    <button
                      onClick={this.props.handleClick}
                      style={{
                        display: "inline",
                        marginLeft: "20px",
                      }}
                    >
                      In Child: Parent ++
                    </button>
                    <button
                      onClick={this.handleChildBtnClick}
                      style={{
                        display: "inline",
                        marginLeft: "20px",
                      }}
                    >
                      In Child: Child ++
                    </button>
                  </div>
                </div>
              );
            }
          }
          
          export default ChildComponent;
          
==================================================================================================
Create a Class Component to Show the User Interface
==================================================================================================
    
    Create a class Component to show the user interface
        
        .. code-block:: cfg
          :caption: src/ClassComponentsDisplay.tsx
          :linenos:
          
          import React from "react";
          import ParentComponentNoChild from "./ParentComponentNoChild";
          import ParentComponentWithChild from "./ParentComponentWithChild";
          import "./list-style.css";
          
          class ClassComponentsDisplay extends React.Component {
            render() {
              return (
                <div className="list-container">
                  <h2>Using State in a React Class Component</h2>
                  <ol>
                    <li className="list-item">
                      <div className="list-item-number"></div>
                      <div className="list-item-content">
                        <h3>Parent Counter -- No Child</h3>
                        <ParentComponentNoChild />
                      </div>
                    </li>
                    <li className="list-item">
                      <div className="list-item-number"></div>
                      <div className="list-item-content">
                        <h3>Parent Counter -- With Child</h3>
                        <ParentComponentWithChild />
                      </div>
                    </li>
                  </ol>
                </div>
              );
            }
          }
          
          export default ClassComponentsDisplay;
          
    - Edit ``App.tsx`` to render the component
        
        .. code-block:: tsx
          :caption: src/App.tsx
          :linenos:
          
          import "./App.css";
          import ClassComponentsDisplay from "./ClassComponentsDisplay";
          
          function App() {
            return <ClassComponentsDisplay />;
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
        - set base to ``/react-projects/react-projects-with-typescript/tut04-class-components-state/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: '/react-projects/react-projects-with-typescript/tut04-class-components-state/',
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut04-class-components-state/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut04-class-components-state/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut04-class-components-state/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut04-class-components-state
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut04-class-components-state/
    - Screenshot
        
        .. figure:: images/tut04/tut04-class-components-state.png
           :align: center
           :class: sd-my-2
           :width: 80%
           :alt: React Class Components - State
           
           :custom-color-primary-bold:`React Class Components - State`