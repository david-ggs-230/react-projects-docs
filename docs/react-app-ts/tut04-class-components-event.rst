.. _tut04-class-components-event:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Class Components - Event
##################################################################################################

Events are just some actions performed by a user to interact with any application. They can be the smallest of actions, like hovering a mouse pointer on an element that triggers a drop-down menu, resizing an application window, or dragging and dropping elements to upload them etc. In React class components, event handling refers to the process of responding to user actions, such as clicks, form submissions, or key presses. React provides a way to handle events in a declarative way, making it easy to respond to user actions and update the component's state or behavior accordingly.

Events in React are divided into three categories:
    
    - Mouse Events − onClick, onDrag, onDoubleClick
    - Keyboard Events − onKeyDown, onKeyPress, onKeyUp
    - Focus Events − onFocus, onBlur
    
Event Handling in React Class Components:
    
    - Binding Event Handlers: In class components, event handler methods need to be bound to the class instance, otherwise, this will not refer to the correct object. This is typically done in the constructor.
    - Event Handlers: Event handler functions are usually methods inside the class component. These methods are invoked when the event is triggered.
    - Using JSX for Event Handling: React uses JSX to attach event handlers, and events in React are camelCased, like onClick, onChange, etc.
    

React event handling is very similar to DOM events with little changes. In JavaScript, when an event is specified, you will be dealing with a react event type called a synthetic event instead of regular DOM events. SyntheticEvent is expensive in terms of CPU resources as every synthetic event created needs to be garbage-collected. Every synthetic event object has the following attributes:
    
    - boolean bubbles
    - boolean cancelable
    - DOMEventTarget currentTarget
    - boolean defaultPrevented
    - number eventPhase
    - boolean isTrusted
    - DOMEvent nativeEvent
    - void preventDefault()
    - boolean isDefaultPrevented()
    - void stopPropagation()
    - boolean isPropagationStopped()
    - void persist()
    - DOMEventTarget target
    - number timeStamp
    - string type
    
Event Handler in Class Component:
    
    - using regular function
        
        - Define the event handler ::
            
            # Passing no argument
            eventHandlerMethod() { 
               .... 
            }
            
            # Passing an event argument
            eventHandlerMethod(e) { 
               .... 
            }
            
            # Passing extra arguments 
            eventHandlerMethod(extra, e) { 
               .... 
            }
            
        - Use the event handler
            
            - must bind the event handler method in the constructor of the component ::
                
                constructor(props) { 
                   ... 
                   this.eventHandlerMethod = this.eventHandlerMethod.bind(this); 
                }
                
            - Handle event on element ::
                
                # Passing no argument
                <tag onClick={this.eventHandlerMethod}> ... </tag>
                <tag onClick={()=>this.eventHandlerMethod()}> ... </tag>
                
                #Passing an event argument
                <tag onClick={this.eventHandlerMethod}> ... </tag>
                <tag onClick={(e)=>this.eventHandlerMethod(e)}> ... </tag>
                
                #Passing extra arguments 
                <tag onClick={this.eventHandlerMethod.bind(this, extra)}> ... </tag>
                <tag onClick={(e)=>this.eventHandlerMethod(extra, e)}> ... </tag>
                
    - using lambda function
        
        - Define the event handler ::
            
            # Passing no argument
            eventHandlerMethod = () => { 
               .... 
            }
            
            # Passing an event argument
            eventHandlerMethod = (e) => { 
               .... 
            }
            
            # Passing extra arguments 
            eventHandlerMethod = (extra, e) => { 
               .... 
            }
            
        - Use the event handler
            
            - in lambda syntax, binding is not needed. this keyword will be automatically bound to the event handler method ::
                
                constructor(props) { 
                   ... 
                   //this.eventHandlerMethod = this.eventHandlerMethod.bind(this);  # no need
                }
                
            - Handle event on element ::
                
                # Passing no argument
                <tag onClick={this.eventHandlerMethod}> ... </tag>
                <tag onClick={()=>this.eventHandlerMethod()}> ... </tag>
                
                #Passing an event argument
                <tag onClick={this.eventHandlerMethod}> ... </tag>
                <tag onClick={(e)=>this.eventHandlerMethod(e)}> ... </tag>
                
                #Passing extra arguments 
                <tag onClick={(e)=>this.eventHandlerMethod(extra, e)}> ... </tag>
                


**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut04-class-components-event --template react-ts
        
    - Move inside the ReactJS project folder <tut04-class-components-event> ::
        
        cd tut04-class-components-event
        
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
Create Class Components Using Event Handler
**************************************************************************************************

Event handling in React class components involves defining methods to handle events, binding those methods to the component instance (either manually or using arrow functions), and associating the methods with events in the JSX. Additionally, arguments can be passed to event handlers when necessary using arrow functions. This allows for a more interactive UI that responds to user input.

==================================================================================================
Event Handler (Pass no argument)
==================================================================================================

--------------------------------------------------------------------------------------------------
Event Handler Using Class Method
--------------------------------------------------------------------------------------------------
    
    Define a class component with methods to modify the state data.
        
        .. code-block:: tsx
          :caption: src/ComponentWithClassFunctionEventHandler.tsx
          :linenos:
          
          import React from "react";
          
          interface ComponentState {
            counter: number;
          }
          
          class ComponentWithClassFunctionEventHandler extends React.Component<
            object,
            ComponentState
          > {
            constructor(props: object) {
              super(props);
              this.state = {
                counter: 0,
              };
              this.handleIncrementBtnClick = this.handleIncrementBtnClick.bind(this);
              this.handleDecrementBtnClick = this.handleDecrementBtnClick.bind(this);
            }
            handleIncrementBtnClick() {
              this.setState((prevState) => ({
                counter: prevState.counter + 1,
              }));
            }
          
            handleDecrementBtnClick() {
              this.setState((prevState) => ({
                counter: prevState.counter - 1,
              }));
            }
            render() {
              return (
                <>
                  <div style={{ marginTop: "20px" }}>Counter: {this.state.counter}</div>
                  <div>
                    <button onClick={() => this.handleIncrementBtnClick()}>
                      Increment
                    </button>
                    <button
                      onClick={() => this.handleDecrementBtnClick()}
                      style={{
                        display: "inline",
                        marginLeft: "20px",
                      }}
                    >
                      Decrement
                    </button>
                  </div>
                </>
              );
            }
          }
          
          export default ComponentWithClassFunctionEventHandler;
          
--------------------------------------------------------------------------------------------------
Event Handler Using Arrow Functions
--------------------------------------------------------------------------------------------------
    
    Define a class component with arrow functions to modify the state data..
        
        .. code-block:: tsx
          :caption: src/ComponentWithArrowFunctionEventHandler.tsx
          :linenos:
          
          import React from "react";
          
          interface ComponentState {
            counter: number;
          }
          
          class ComponentWithArrowFunctionEventHandler extends React.Component<
            object,
            ComponentState
          > {
            constructor(props: object) {
              super(props);
              this.state = {
                counter: 0,
              };
            }
            handleIncrementBtnClick = () => {
              this.setState((prevState) => ({
                counter: prevState.counter + 1,
              }));
            };
          
            handleDecrementBtnClick = () => {
              this.setState((prevState) => ({
                counter: prevState.counter - 1,
              }));
            };
            render() {
              return (
                <>
                  <div style={{ marginTop: "20px" }}>Counter: {this.state.counter}</div>
                  <div>
                    <button onClick={this.handleIncrementBtnClick}>Increment</button>
                    <button
                      onClick={this.handleDecrementBtnClick}
                      style={{
                        display: "inline",
                        marginLeft: "20px",
                      }}
                    >
                      Decrement
                    </button>
                  </div>
                </>
              );
            }
          }
          
          export default ComponentWithArrowFunctionEventHandler;
          

==================================================================================================
Event Handler (Pass extra argument)
==================================================================================================

--------------------------------------------------------------------------------------------------
Event Handler Using Class Method
--------------------------------------------------------------------------------------------------
    
    Define a class component with methods to modify the state data.
        
        .. code-block:: tsx
          :caption: src/ComponentWithClassFunctionExtraArgs.tsx
          :linenos:
          
          import React from "react";
          
          interface ComponentState {
            counter: number;
            messages: string[];
          }
          
          class ComponentWithClassFunctionExtraArgs extends React.Component<
            object,
            ComponentState
          > {
            constructor(props: object) {
              super(props);
              this.state = {
                counter: 0,
                messages: [],
              };
              this.handleIncrementBtnClick = this.handleIncrementBtnClick.bind(this);
              this.handleDecrementBtnClick = this.handleDecrementBtnClick.bind(this);
              this.handleMessagesUpdateClick = this.handleMessagesUpdateClick.bind(this);
              this.handleMessagesUpdateEventClick =
                this.handleMessagesUpdateEventClick.bind(this);
            }
            handleIncrementBtnClick() {
              this.setState((prevState) => ({
                counter: prevState.counter + 1,
              }));
            }
          
            handleDecrementBtnClick() {
              this.setState((prevState) => ({
                counter: prevState.counter - 1,
              }));
            }
            handleMessagesUpdateClick({
              message,
              count,
            }: {
              message: string;
              count: number;
            }) {
              this.setState((prevState) => ({
                messages: [...prevState.messages, "" + message + ", count: " + count],
              }));
            }
            handleMessagesUpdateEventClick(
              {
                message,
                count,
              }: {
                message: string;
                count: number;
              },
              e: React.MouseEvent,
            ) {
              this.setState((prevState) => ({
                messages: [
                  ...prevState.messages,
                  "" +
                    message +
                    ", count: " +
                    count +
                    ", e: " +
                    (e?.target as HTMLElement)?.innerHTML,
                ],
              }));
            }
            render() {
              return (
                <>
                  <div style={{ marginTop: "20px" }}>Counter: {this.state.counter}</div>
                  <div>
                    <button onClick={() => this.handleIncrementBtnClick()}>
                      Increment
                    </button>
                    <button
                      onClick={() => this.handleDecrementBtnClick()}
                      style={{
                        display: "inline",
                        marginLeft: "20px",
                      }}
                    >
                      Decrement
                    </button>
                  </div>
                  <div style={{ marginTop: "20px" }}>
                    <button
                      onClick={this.handleMessagesUpdateClick.bind(this, {
                        message: "Button 1",
                        count: this.state.counter,
                      })}
                    >
                      Button 1
                    </button>
                    <button
                      onClick={() =>
                        this.handleMessagesUpdateClick({
                          message: "Button 2",
                          count: this.state.counter,
                        })
                      }
                      style={{ marginLeft: "20px" }}
                    >
                      Button 2
                    </button>
                    
                    <button
                      onClick={(e) =>
                        this.handleMessagesUpdateEventClick(
                          {
                            message: "Button 3",
                            count: this.state.counter,
                          },
                          e,
                        )
                      }
                      style={{ marginLeft: "20px" }}
                    >
                      Button 3
                    </button>
                  </div>
                  {this.state.messages.length > 0 && (
                    <div className="list-container">
                      <h5>LogMessages</h5>
                      <ol>
                        {this.state.messages.map((message, index) => (
                          <li key={index} className="list-item">
                            <div>
                              {index + 1}. {message}
                            </div>
                          </li>
                        ))}
                      </ol>
                    </div>
                  )}
                </>
              );
            }
          }
          
          export default ComponentWithClassFunctionExtraArgs;
          
--------------------------------------------------------------------------------------------------
Event Handler Using Arrow Functions
--------------------------------------------------------------------------------------------------
    
    Define a class component with arrow functions to modify the state data..
        
        .. code-block:: tsx
          :caption: src/ComponentWithArrowFunctionEventHandler.tsx
          :linenos:
          
          import React from "react";
          
          interface ComponentState {
            counter: number;
            messages: string[];
          }
          
          class ComponentWitharrowFunctionExtraArgs extends React.Component<
            object,
            ComponentState
          > {
            constructor(props: object) {
              super(props);
              this.state = {
                counter: 0,
                messages: [],
              };
            }
            handleIncrementBtnClick = () => {
              this.setState((prevState) => ({
                counter: prevState.counter + 1,
              }));
            };
          
            handleDecrementBtnClick = () => {
              this.setState((prevState) => ({
                counter: prevState.counter - 1,
              }));
            };
            handleMessagesUpdateClick = ({
              message,
              count,
            }: {
              message: string;
              count: number;
            }) => {
              this.setState((prevState) => ({
                messages: [...prevState.messages, "" + message + ", count: " + count],
              }));
            };
            handleMessagesUpdateEventClick = (
              {
                message,
                count,
              }: {
                message: string;
                count: number;
              },
              e: React.MouseEvent,
            ) => {
              this.setState((prevState) => ({
                messages: [
                  ...prevState.messages,
                  "" +
                    message +
                    ", count: " +
                    count +
                    ", e: " +
                    (e?.target as HTMLElement)?.innerHTML,
                ],
              }));
            };
            render() {
              return (
                <>
                  <div style={{ marginTop: "20px" }}>Counter: {this.state.counter}</div>
                  <div>
                    <button onClick={() => this.handleIncrementBtnClick()}>
                      Increment
                    </button>
                    <button
                      onClick={() => this.handleDecrementBtnClick()}
                      style={{
                        display: "inline",
                        marginLeft: "20px",
                      }}
                    >
                      Decrement
                    </button>
                  </div>
                  <div style={{ marginTop: "20px" }}>
                    <button
                      onClick={this.handleMessagesUpdateClick.bind(this, {
                        message: "Button 1",
                        count: this.state.counter,
                      })}
                    >
                      Button 1
                    </button>
                    <button
                      onClick={() =>
                        this.handleMessagesUpdateClick({
                          message: "Button 2",
                          count: this.state.counter,
                        })
                      }
                      style={{ marginLeft: "20px" }}
                    >
                      Button 2
                    </button>
          
                    <button
                      onClick={(e) =>
                        this.handleMessagesUpdateEventClick(
                          {
                            message: "Button 3",
                            count: this.state.counter,
                          },
                          e,
                        )
                      }
                      style={{ marginLeft: "20px" }}
                    >
                      Button 3
                    </button>
                  </div>
                  {this.state.messages.length > 0 && (
                    <div className="list-container">
                      <h5>LogMessages</h5>
                      <ol>
                        {this.state.messages.map((message, index) => (
                          <li key={index} className="list-item">
                            <div>
                              {index + 1}. {message}
                            </div>
                          </li>
                        ))}
                      </ol>
                    </div>
                  )}
                </>
              );
            }
          }
          
          export default ComponentWitharrowFunctionExtraArgs;
          
==================================================================================================
Create a Class Component to Show the User Interface
==================================================================================================
    
    - Create a class Component to show the user interface
        
        .. code-block:: tsx
          :caption: src/ClassComponentsDisplay.tsx
          :linenos:
          
          import React from "react";
          import ComponentWithClassFunctionEventHandler from "./ComponentWithClassFunctionEventHandler";
          import ComponentWithArrowFunctionEventHandler from "./ComponentWithArrowFunctionEventHandler";
          import ComponentWithClassFunctionExtraArgs from "./ComponentWithClassFunctionExtraArgs";
          import ComponentWitharrowFunctionExtraArgs from "./ComponentWitharrowFunctionExtraArgs";
          import "./list-style.css";
          
          class ClassComponentsDisplay extends React.Component {
            render() {
              return (
                <div className="list-container">
                  <h2>Event Handling in a React Class Component</h2>
                  <ol>
                    <li className="list-item">
                      <div className="list-item-number"></div>
                      <div className="list-item-content">
                        <h3>Event Handler by Class Methods</h3>
                        <ComponentWithClassFunctionEventHandler />
                      </div>
                    </li>
                    <li className="list-item">
                      <div className="list-item-number"></div>
                      <div className="list-item-content">
                        <h3>Event Handler by Arrow Functions</h3>
                        <ComponentWithArrowFunctionEventHandler />
                      </div>
                    </li>
                    <li className="list-item">
                      <div className="list-item-number"></div>
                      <div className="list-item-content">
                        <h3>Event Handler by Class Methods with Extra Arguments</h3>
                        <ComponentWithClassFunctionExtraArgs />
                      </div>
                    </li>
                    <li className="list-item">
                      <div className="list-item-number"></div>
                      <div className="list-item-content">
                        <h3>Event Handler by Arrow Functions with Extra Arguments</h3>
                        <ComponentWitharrowFunctionExtraArgs />
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
        - set base to ``/react-projects/react-projects-with-typescript/tut04-class-components-event/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut04-class-components-event/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut04-class-components-event/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut04-class-components-event/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut04-class-components-event/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut04-class-components-event
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut04-class-components-event/
    - Screenshot
        
        .. figure:: images/tut04/tut04-class-components-event.png
           :align: center
           :class: sd-my-2
           :width: 80%
           :alt: React Class Components - Event
           
           :custom-color-primary-bold:`React Class Components - Event`