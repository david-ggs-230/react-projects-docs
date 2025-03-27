.. _tut04-class-components-life-cycle:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Class Components - Life Cycle
##################################################################################################

Each React component has three distinct stages:
    
    - Mounting − Mounting represents the rendering of the React component in the given DOM node.
        
        - constructor()
            
            Invoked during the initial construction phase of the React component. Used to set initial state and properties of the component.
            
        - getDerivedStateFromProps()
            
            Invoked during both initial and update phase and just before the render() method. It is mostly used in animation context where the various state of the component is needed to do smooth animation. The signature of the API is: :custom-color-primary-bold:`static getDerivedStateFromProps(props, state)`
                
                - props − current properties of the component
                - state − Current state of the component
                
            
        - render()
            
            It renders the component in the virtual DOM instance. This is specified as mounting of the component in the DOM tree.
            
        - componentDidMount()
            
            Invoked after the initial mounting of the component in the DOM tree.
            
        
    - Updating − Updating represents the re-rendering of the React component in the given DOM node during state changes / updates.
        
        - shouldComponentUpdate()
            
            Invoked during the update phase. Used to specify whether the component should update or not. The signature of the API is: :custom-color-primary-bold:`shouldComponentUpdate(nextProps, nextState)`
                
                - nextProps − Upcoming properties of the component
                - nextState − Upcoming state of the component
                
            
        - getDerivedStateFromProps()
            
            Invoked during both initial and update phase and just before the render() method. It is mostly used in animation context where the various state of the component is needed to do smooth animation. The signature of the API is: :custom-color-primary-bold:`static getDerivedStateFromProps(props, state)`
                
                - props − current properties of the component
                - state − Current state of the component
                
            
        - render()
            
            It renders the component in the virtual DOM instance. 
            
        - getSnapshotBeforeUpdate()
            
            Invoked just before the rendered content is commited to DOM tree. The data returned by this method will be passed to ComponentDidUpdate() method. The signature of the API is: :custom-color-primary-bold:`getSnapshotBeforeUpdate(prevProps, prevState)`
                
                - prevProps − Previous properties of the component.
                - prevState − Previous state of the component.
                
            
            
        - componentDidUpdate()
            
            Invoked during the update phase. The signature of the API is: :custom-color-primary-bold:`componentDidUpdate(prevProps, prevState, snapshot)`
                
                - prevProps − Previous properties of the component.
                - prevState − Previous state of the component.
                - snapshot − Current rendered content.
                
            
        
    - Unmounting − Unmounting represents the removal of the React component.
        
        - componentWillUnmount() 
            
            Invoked after the component is unmounted from the DOM. This is the good place to clean up the object.
            
        
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut04-class-components-life-cycle --template react-ts
        
    - Move inside the ReactJS project folder <tut04-class-components-life-cycle> ::
        
        cd tut04-class-components-life-cycle
        
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
Create Class Components Showing Life Cycles
**************************************************************************************************

Life Cycle Stages:
    
    - Mounting
        - constructor()
        - getDerivedStateFromProps()
        - render()
        - componentDidMount()
    - Updating
        - shouldComponentUpdate()
        - getDerivedStateFromProps()
        - render()
        - getSnapshotBeforeUpdate()
        - componentDidUpdate()
    - Unmounting
        - componentWillUnmount()

==================================================================================================
Class Components with Life Cycle Methods
==================================================================================================

    
    Define a class component with life cycle methods.
        
        .. code-block:: tsx
          :caption: src/ComponentLifeCycle.tsx
          :linenos:
          
          import React from "react";
          interface ComponentLifeCycleState {
            count: number;
            rerender: boolean;
          }
          
          class ComponentLifeCycle extends React.Component<
            object,
            ComponentLifeCycleState
          > {
            static logMessages: string[] = [];
            constructor(props: object) {
              super(props);
              this.state = {
                count: 0,
                rerender: true,
              };
              if (!ComponentLifeCycle.logMessages) ComponentLifeCycle.logMessages = [];
              ComponentLifeCycle.logMessages.push(
                "constructor(), count: " + this.state.count,
              );
            }
          
            static getDerivedStateFromProps(
              props: object,
              state: ComponentLifeCycleState,
            ): Partial<ComponentLifeCycleState> | null {
              ComponentLifeCycle.logMessages.push(
                "getDerivedStateFromProps(), count: " + state.count,
              );
              return null;
            }
          
            componentDidMount() {
              ComponentLifeCycle.logMessages.push(
                "componentDidMount(), count: " + this.state.count,
              );
            }
          
            shouldComponentUpdate(nextProps: object, nextState: ComponentLifeCycleState) {
              ComponentLifeCycle.logMessages.push(
                "shouldComponentUpdate(), count: " + nextState.count,
              );
              return true;
            }
          
            getSnapshotBeforeUpdate(
              nextProps: object,
              nextState: ComponentLifeCycleState,
            ) {
              ComponentLifeCycle.logMessages.push(
                "getSnapshotBeforeUpdate(), count: " + this.state.count,
              );
              return nextState.count;
            }
          
            componentDidUpdate() {
              ComponentLifeCycle.logMessages.push(
                "componentDidUpdate(), count: " + this.state.count,
              );
            }
          
            componentWillUnmount() {
              ComponentLifeCycle.logMessages.push(
                "componentWillUnmount(), count: " + this.state.count,
              );
            }
          
            handleIncrement = () => {
              this.setState({ count: this.state.count + 1 });
              ComponentLifeCycle.logMessages.push(
                "handleIncrement (), count: " + this.state.count,
              );
            };
          
            render() {
              ComponentLifeCycle.logMessages.push("render(), count: " + this.state.count);
              return (
                <>
                  <div className="list-container">
                    <h2>Class Component Life Cycle</h2>
                    <p>
                      Count: {this.state.count}{" "}
                      <button onClick={this.handleIncrement}>Increment</button>
                    </p>
                    <h4>Log Messages:</h4>
                    <ol>
                      {ComponentLifeCycle.logMessages.map((message, index) => (
                        <li key={index} className="list-item" style={{ margin: "1px" }}>
                          <div>
                            {index + 1}. {message}
                          </div>
                        </li>
                      ))}
                    </ol>
                  </div>
                </>
              );
            }
          }
          
          export default ComponentLifeCycle;
          
==================================================================================================
Create a Class Component to Show the User Interface
==================================================================================================
    
    - Create a class Component to show the user interface
        
        .. code-block:: tsx
          :caption: src/ClassComponentsDisplay.tsx
          :linenos:
          
          import React from "react";
          import ComponentLifeCycle from "./ComponentLifeCycle";
          import "./list-style.css";
          
          class ClassComponentsDisplay extends React.Component {
            render() {
              return <ComponentLifeCycle />;
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
          
**************************************************************************************************
Hosting the React App on GitHub Pages
**************************************************************************************************

==================================================================================================
Build the App
==================================================================================================
    
    - Configure the ts build options:
        
        - open tsconfig.app.json file
        - set "noUnusedParameters": false, as some parameters are place-holders required for life cycle functions ::
            
            /* Linting */
            "strict": true,
            "noUnusedLocals": true,
            "noUnusedParameters": false,
            "noFallthroughCasesInSwitch": true,
            "noUncheckedSideEffectImports": true
            
    - Configure the build base url:
        
        - open vite.config.js file
        - set base to ``/react-projects/react-projects-with-typescript/tut04-class-components-life-cycle/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut04-class-components-life-cycle/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut04-class-components-life-cycle/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut04-class-components-life-cycle/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut04-class-components-life-cycle/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut04-class-components-life-cycle
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut04-class-components-life-cycle/
    - Screenshot
        
        .. figure:: images/tut04/tut04-class-components-life-cycle.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Class Components - Life Cycles
           
           :custom-color-primary-bold:`React Class Components - Life Cycles`