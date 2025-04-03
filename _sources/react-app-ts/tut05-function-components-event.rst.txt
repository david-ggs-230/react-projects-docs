.. _tut05-function-components-event:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Function Components - Event
##################################################################################################

Events are just some actions performed by a user to interact with any application. They can be the smallest of actions, like hovering a mouse pointer on an element that triggers a drop-down menu, resizing an application window, or dragging and dropping elements to upload them etc. In React Function Components, event handling refers to the process of responding to user actions, such as clicks, form submissions, or key presses. React provides a way to handle events in a declarative way, making it easy to respond to user actions and update the component's state or behavior accordingly.

Events in React are divided into three categories:
    
    - Mouse Events − onClick, onDrag, onDoubleClick
    - Keyboard Events − onKeyDown, onKeyPress, onKeyUp
    - Focus Events − onFocus, onBlur
    
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
    
Event Handler in Function Component:
    
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
            
        - Use the event handler ::
            
            # Passing no argument
            <tag onClick={eventHandlerMethod}> ... </tag>
            
            #Passing an event argument
            <tag onClick={eventHandlerMethod}> ... </tag>
            
            #Passing extra arguments 
            <tag onClick={eventHandlerMethod.bind(this, extra)}> ... </tag>
            <tag onClick={(e)=>eventHandlerMethod(extra, e)}> ... </tag>
            
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
            
        - Use the event handler ::
            
            # Passing no argument
            <tag onClick={eventHandlerMethod}> ... </tag>
            
            #Passing an event argument
            <tag onClick={eventHandlerMethod}> ... </tag>
            
            #Passing extra arguments 
            <tag onClick={eventHandlerMethod.bind(null, extra)}> ... </tag>
            <tag onClick={(e)=>eventHandlerMethod(extra, e)}> ... </tag>
            

**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut05-function-components-event --template react-ts
        
    - Move inside the ReactJS project folder <tut05-function-components-event> ::
        
        cd tut05-function-components-event
        
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
Create Function Components Using Event Handler
**************************************************************************************************

Event handling in React Function Components involves defining methods to handle events, and associating the methods with events in the JSX. Additionally, arguments can be passed to event handlers when necessary using arrow functions. This allows for a more interactive UI that responds to user input.

==================================================================================================
Event Handler (Pass no argument)
==================================================================================================

--------------------------------------------------------------------------------------------------
Event Handler Using Function Method
--------------------------------------------------------------------------------------------------
    
    Define a Function Component with methods to modify the state data.
        
        .. code-block:: tsx
          :caption: src/FunctionComponentWithEventHandlerWithNoArgs.tsx
          :linenos:
          
          import React, { useState } from "react";
          
          const FunctionComponentWithEventHandlerWithNoArgs: React.FC = () => {
            const [counter, setCounter] = useState(0);
          
            function handleIncrementBtnClick() {
              setCounter((prevCounter) => prevCounter + 1);
            }
          
            function handleDecrementBtnClick() {
              setCounter((prevCounter) => prevCounter - 1);
            }
          
            return (
              <>
                <div style={{ marginTop: "20px" }}>Counter: {counter}</div>
                <div>
                  <button onClick={handleIncrementBtnClick}>Increment</button>
                  <button
                    onClick={handleDecrementBtnClick}
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
          };
          
          export default FunctionComponentWithEventHandlerWithNoArgs;
          
--------------------------------------------------------------------------------------------------
Event Handler Using Arrow Functions
--------------------------------------------------------------------------------------------------
    
    Define a Function Component with arrow functions to modify the state data..
        
        .. code-block:: tsx
          :caption: src/FunctionComponentWithArrowFunctionWithNoArgs.tsx
          :linenos:
          
          import React, { useState } from "react";
          
          const FunctionComponentWithArrowFunctionWithNoArgs: React.FC = () => {
            const [counter, setCounter] = useState(0);
          
            const handleIncrementBtnClick = () => {
              setCounter((prevCounter) => prevCounter + 1);
            };
          
            const handleDecrementBtnClick = () => {
              setCounter((prevCounter) => prevCounter - 1);
            };
          
            return (
              <>
                <div style={{ marginTop: "20px" }}>Counter: {counter}</div>
                <div>
                  <button onClick={handleIncrementBtnClick}>Increment</button>
                  <button
                    onClick={handleDecrementBtnClick}
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
          };
          
          export default FunctionComponentWithArrowFunctionWithNoArgs;
          
==================================================================================================
Event Handler (Pass extra argument)
==================================================================================================

--------------------------------------------------------------------------------------------------
Event Handler Using Function Method
--------------------------------------------------------------------------------------------------
    
    Define a Function Component with methods to modify the state data.
        
        .. code-block:: tsx
          :caption: src/FunctionComponentWithEventHandlerWithExtraArgs.tsx
          :linenos:
          
          import React, { useState } from "react";
          
          const FunctionComponentWithEventHandlerWithExtraArgs: React.FC = () => {
            const [counter, setCounter] = useState(0);
            const [messages, setMessages] = useState([] as string[]);
            function handleIncrementBtnClick() {
              setCounter((prevCounter) => prevCounter + 1);
            }
          
            function handleDecrementBtnClick() {
              setCounter((prevCounter) => prevCounter - 1);
            }
            function handleMessagesUpdateClick({
              message,
              count,
            }: {
              message: string;
              count: number;
            }) {
              setMessages((prevState) => [
                ...prevState,
                `${message}, Current counter: ${count}`,
              ]);
            }
            function handleMessagesUpdateClickWithEvent(
              {
                message,
                count,
              }: {
                message: string;
                count: number;
              },
              event: React.MouseEvent,
            ) {
              setMessages((prevState) => [
                ...prevState,
                `${message}, Current counter: ${count}, e: ${(event?.target as HTMLElement)?.innerHTML}`,
              ]);
            }
            return (
              <>
                <div>
                  <div style={{ marginTop: "20px" }}>Counter: {counter}</div>
                  <div>
                    <button onClick={handleIncrementBtnClick}>Increment</button>
                    <button
                      onClick={handleDecrementBtnClick}
                      style={{
                        display: "inline",
                        marginLeft: "20px",
                      }}
                    >
                      Decrement
                    </button>
                  </div>
                </div>
                <div style={{ marginTop: "20px" }}>
                  <button
                    onClick={handleMessagesUpdateClick.bind(this, {
                      message: "Button 1",
                      count: counter,
                    })}
                  >
                    Button 1
                  </button>
                  <button
                    onClick={() =>
                      handleMessagesUpdateClick({
                        message: "Button 2",
                        count: counter,
                      })
                    }
                    style={{ marginLeft: "20px" }}
                  >
                    Button 2
                  </button>
          
                  <button
                    onClick={(e) =>
                      handleMessagesUpdateClickWithEvent(
                        {
                          message: "Button 3",
                          count: counter,
                        },
                        e,
                      )
                    }
                    style={{ marginLeft: "20px" }}
                  >
                    Button 3
                  </button>
                </div>
                <div>
                  {messages.length > 0 && (
                    <div className="list-container">
                      <h5>LogMessages</h5>
                      <ol>
                        {messages.map((message, index) => (
                          <li key={index} className="list-item">
                            <div>
                              {index + 1}. {message}
                            </div>
                          </li>
                        ))}
                      </ol>
                    </div>
                  )}
                </div>
              </>
            );
          };
          
          export default FunctionComponentWithEventHandlerWithExtraArgs;
          
--------------------------------------------------------------------------------------------------
Event Handler Using Arrow Functions
--------------------------------------------------------------------------------------------------
    
    Define a Function Component with arrow functions to modify the state data..
        
        .. code-block:: tsx
          :caption: src/FunctionComponentWithArrowFunctionWithExtraArgs.tsx
          :linenos:
          
          import React, { useState } from "react";
          
          const FunctionComponentWithArrowFunctionWithExtraArgs: React.FC = () => {
            const [counter, setCounter] = useState(0);
            const [messages, setMessages] = useState([] as string[]);
            const handleIncrementBtnClick = () => {
              setCounter((prevCounter) => prevCounter + 1);
            };
            const handleDecrementBtnClick = () => {
              setCounter((prevCounter) => prevCounter - 1);
            };
            const handleMessagesUpdateClick = ({
              message,
              count,
            }: {
              message: string;
              count: number;
            }) => {
              setMessages((prevState) => [
                ...prevState,
                `${message}, Current counter: ${count}`,
              ]);
            };
            const handleMessagesUpdateClickWithEvent = (
              { message, count }: { message: string; count: number },
              event: React.MouseEvent,
            ) => {
              setMessages((prevState) => [
                ...prevState,
                `${message}, Current counter: ${count}, e: ${(event?.target as HTMLElement)?.innerHTML}`,
              ]);
            };
          
            return (
              <>
                <div>
                  <div style={{ marginTop: "20px" }}>Counter: {counter}</div>
                  <div>
                    <button onClick={handleIncrementBtnClick}>Increment</button>
                    <button
                      onClick={handleDecrementBtnClick}
                      style={{
                        display: "inline",
                        marginLeft: "20px",
                      }}
                    >
                      Decrement
                    </button>
                  </div>
                </div>
                <div style={{ marginTop: "20px" }}>
                  <button
                    onClick={handleMessagesUpdateClick.bind(this, {
                      message: "Button 1",
                      count: counter,
                    })}
                  >
                    Button 1
                  </button>
                  <button
                    onClick={() =>
                      handleMessagesUpdateClick({
                        message: "Button 2",
                        count: counter,
                      })
                    }
                    style={{ marginLeft: "20px" }}
                  >
                    Button 2
                  </button>
          
                  <button
                    onClick={(e) =>
                      handleMessagesUpdateClickWithEvent(
                        {
                          message: "Button 3",
                          count: counter,
                        },
                        e,
                      )
                    }
                    style={{ marginLeft: "20px" }}
                  >
                    Button 3
                  </button>
                </div>
                <div>
                  {messages.length > 0 && (
                    <div className="list-container">
                      <h5>LogMessages</h5>
                      <ol>
                        {messages.map((message, index) => (
                          <li key={index} className="list-item">
                            <div>
                              {index + 1}. {message}
                            </div>
                          </li>
                        ))}
                      </ol>
                    </div>
                  )}
                </div>
              </>
            );
          };
          
          export default FunctionComponentWithArrowFunctionWithExtraArgs;
          
==================================================================================================
Create a Function Component to Show the User Interface
==================================================================================================
    
    - Create a Function Component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import FunctionComponentWithEventHandlerWithNoArgs from "./FunctionComponentWithEventHandlerWithNoArgs";
          import FunctionComponentWithArrowFunctionWithNoArgs from "./FunctionComponentWithArrowFunctionWithNoArgs";
          import FunctionComponentWithEventHandlerWithExtraArgs from "./FunctionComponentWithEventHandlerWithExtraArgs";
          import FunctionComponentWithArrowFunctionWithExtraArgs from "./FunctionComponentWithArrowFunctionWithExtraArgs";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>Event Handling in a React Function Component</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Event Handler by Function Methods</h3>
                      <h5
                        className="blue-color"
                        style={{ marginTop: "0px", marginBottom: "0px" }}
                      >
                        EventHandler: function without arguments
                      </h5>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Signature: function xxxhandler(){"{...}"}
                      </h5>
                      <div>
                        <FunctionComponentWithEventHandlerWithNoArgs />
                      </div>
                    </div>
                  </li>
          
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Event Handler by Arrow Functions</h3>
                      <h5
                        className="blue-color"
                        style={{ marginTop: "0px", marginBottom: "0px" }}
                      >
                        EventHandler: arrow function without arguments
                      </h5>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Signature: const xxxhandler=(){" => {...}"}
                      </h5>
                      <div>
                        <FunctionComponentWithArrowFunctionWithNoArgs />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Event Handler by Function Methods with Extra Arguments</h3>
                      <h5
                        className="blue-color"
                        style={{ marginTop: "0px", marginBottom: "0px" }}
                      >
                        EventHandler: function with extra arguments
                      </h5>
                      <h5
                        className="blue-color"
                        style={{ marginTop: "0px", marginBottom: "0px" }}
                      >
                        Signature: function xxxhandler{"({arg1,arg2}){...}"}
                      </h5>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Signature: function xxxhandler{"({arg1,arg2}, event){...}"}
                      </h5>
                      <div>
                        <FunctionComponentWithEventHandlerWithExtraArgs />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Event Handler by Arrow Function with Extra Arguments</h3>
                      <h5
                        className="blue-color"
                        style={{ marginTop: "0px", marginBottom: "0px" }}
                      >
                        EventHandler: arrow function with extra arguments
                      </h5>
                      <h5
                        className="blue-color"
                        style={{ marginTop: "0px", marginBottom: "0px" }}
                      >
                        Signature: const xxxhandler{"=({arg1,arg2}) => {...}"}
                      </h5>
                      <h5 className="blue-color" style={{ marginTop: "0px" }}>
                        Signature: const xxxhandler{"=({arg1,arg2}, event) => {...}"}
                      </h5>
                      <div>
                        <FunctionComponentWithArrowFunctionWithExtraArgs />
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
          import "./list-style.css";
          
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
        - set base to ``/react-projects/react-projects-with-typescript/tut05-function-components-event/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut05-function-components-event/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-event/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut05-function-components-event/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut05-function-components-event/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut05-function-components-event
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut05-function-components-event/
    - Screenshot
        
        .. figure:: images/tut05/tut05-function-components-event.png
           :align: center
           :class: sd-my-2
           :width: 80%
           :alt: React Function Components - Event
           
           :custom-color-primary-bold:`React Function Components - Event`