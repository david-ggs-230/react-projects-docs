.. _tut07-react-restapi:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React RESTful API
##################################################################################################

**************************************************************************************************
Introduction
**************************************************************************************************

Integrating RESTful APIs with React enhances the functionality of web applications by enabling them to fetch and update data dynamically. This integration facilitates a seamless user experience, ensuring that the application remains responsive and up-to-date.
    
Make API Requests in React:
    
    - Using the fetch API − The fetch API is a built-in JavaScript method for making network requests.
    - Using axios library for HTTP Requests − axios is a popular library for making HTTP requests.
    

==================================================================================================
The Fetch API
==================================================================================================

The Fetch API is a modern interface for making HTTP requests in the browser. It provides a more powerful and flexible way to handle network requests compared to older techniques like XMLHttpRequest. The fetch function is used to make a GET request to the specified API endpoint, and the response is converted to JSON using response.json().
    
    - Making GET Requests
        
        - GET request ::
            
            const [data, setData] = useState([]);
            
            useEffect(() => {
              const fetchData = async () => {
                try {
                  const response = await fetch('http://localhost:3001/posts');
                  const result = await response.json();
                  setData(result);
                } catch (error) {
                  console.error('Error fetching data:', error);
                }
              };  
              fetchData();
            }, []);
            
        - GET request with query parameters ::
            
            const [data, setData] = useState([]);
            const [loading, setLoading] = useState(true);
            
            // with setTimeout
            useEffect(() => {
              const fetchData = async () => {
                try {
                  // Simulating a delay to show loading state
                  setTimeout(async () => {
                    const response = await fetch('http://localhost:3001/posts?id=1');
                    const result = await response.json();
                    setData(result);
                    setLoading(false);
                  }, 1000);
                } catch (error) {
                  console.error('Error fetching data:', error);
                  setLoading(false);
                }
              };
            
              fetchData();
            }, []);
            
            
        - GET request with query parameters ::
            
            const [data, setData] = useState([]);
            const [loading, setLoading] = useState(true);
            
            useEffect(() => {
              const fetchData = async () => {
                fetch('http://localhost:3001/posts?id=1')
                        .then((response) => response.json())
                        .then((result) => {
                            setData(result);
                            setLoading(false);
                        })
                        .catch((err) => {
                            console.error('Error fetching data:', error);
                            setLoading(false);
                        });
              };
              
              fetchData();
            }, []);
            
    - Making POST Requests
        
        - POST request ::
            
            const [posts, setPosts] = useState ([]);
            const [title, setTitle] = useState('');
            const [body, setBody] = useState('');
            // ...
            const addPosts = async (title, body) => {
               await fetch('http://localhost:3001/posts', {
                  method: 'POST',
                  body: JSON.stringify({
                     title: title,
                     body: body,
                     userId: Math.random().toString(36).slice(2),
                  }),
                  headers: {
                     'Content-type': 'application/json; charset=UTF-8',
                  },
               })
                  .then((response) => response.json())
                  .then((data) => {
                     setPosts((posts) => [data, ...posts]);
                     setTitle('');
                     setBody('');
                  })
                  .catch((err) => {
                     console.log(err.message);
                  });
            };
            
            const handleSubmit = (e) => {
               e.preventDefault();
               addPosts(title, body);
            };    
            
==================================================================================================
The axios library
==================================================================================================
Axios is an HTTP client library based on promises that makes it simple to send asynchronous HTTP requests to REST endpoints. 
    
    - Install Axios by running the following command ::
        
        # npm
        npm install axios
        # yarn
        yarn add axios
        
    - Create an instance ::
        
        import axios from "axios";
        
        const client = axios.create({
           baseURL: 'http://localhost:3001/posts' 
        });
        
    - Perform a GET Request in React With Axios ::
        
        useEffect(() => {
           client.get('?id=10').then((response) => {
              setPosts(response.data);
           });
        }, []);
        
    - Perform a POST Request in React With Axios ::
        
        const addPosts = (title, body) => {
           client
              .post('', {
                 title: title,
                 body: body,
              })
              .then((response) => {
                 setPosts((posts) => [response.data, ...posts]);
              });
        };
        
    - Perform a DELETE Request in React With Axios ::
        
        const deletePost = (id) => {
           client.delete(`${id}`);
           setPosts(
              posts.filter((post) => {
                 return post.id !== id;
              })
           );
        };
        
    - Use Async/Await in Axios ::
        
        import React, { useState, useEffect } from 'react';
        
        const App = () => {
           const [title, setTitle] = useState('');
           const [body, setBody] = useState('');
           const [posts, setPosts] = useState([]);
        
           // GET with Axios
           useEffect(() => {
              const fetchPost = async () => {
                 let response = await client.get('?_limit=10');
                 setPosts(response.data);
              };
              fetchPost();
           }, []);
        
           // Delete with Axios
           const deletePost = async (id) => {
              await client.delete(`${id}`);
              setPosts(
                 posts.filter((post) => {
                    return post.id !== id;
                 })
              );
           };
        
           // Post with Axios
           const addPosts = async (title, body) => {
              let response = await client.post('', {
                 title: title,
                 body: body,
              });
              setPosts((posts) => [response.data, ...posts]);
           };
        
           const handleSubmit = (e) => {
              e.preventDefault();
              addPosts(title, body);
           };
        
           return (
              // ...
           );
        };
        
        export default App;
        
    

**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut07-react-restapi --template react-ts
        
    - Move inside the ReactJS project folder <tut07-react-restapi> ::
        
        cd tut07-react-restapi
        
    - Install the dependencies ::
        
        yarn install
        
    - Install library dependencies ::
        
        yarn add axios react-hook-form
        
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
React RESTful API Components
**************************************************************************************************

==================================================================================================
Controlled Components
==================================================================================================
    
    - Define a controlled react form function component.
        
        .. code-block:: tsx
          :caption: src/ReactFormControlledComponent.tsx
          :linenos:
          
          import React, { useState } from "react";
          import "./App.css";
          
          const ReactFormControlledComponent: React.FC = () => {
            const [formState, setFormState] = useState({
              name: "",
              age: "",
              location: "",
            });
            const labelStyle = {
              display: "inline-block",
              width: "2.5rem",
              marginRight: "1.5rem",
            };
            const changeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
              const { name, value } = e.target;
              setFormState((prevState) => ({ ...prevState, [name]: value }));
            };
          
            const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
              e.preventDefault();
              alert(JSON.stringify(formState));
            };
          
            return (
              <div>
                <div className="App">
                  <form onSubmit={handleSubmit}>
                    <div style={{ marginTop: 20 }}>
                      <label htmlFor="name" style={labelStyle}>
                        Name
                      </label>
                      <input
                        type="text"
                        id="name"
                        name="name"
                        placeholder="Enter name"
                        value={formState.name}
                        onChange={changeHandler}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="age" style={labelStyle}>
                        Age
                      </label>
                      <input
                        type="number"
                        id="age"
                        name="age"
                        placeholder="Enter age"
                        value={formState.age}
                        onChange={changeHandler}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="location" style={labelStyle}>
                        Location
                      </label>
                      <input
                        type="text"
                        id="location"
                        name="location"
                        placeholder="Enter location"
                        value={formState.location}
                        onChange={changeHandler}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <input type="submit" value="Submit" />
                    </div>
                  </form>
                </div>
                <div>
                  <h4 style={{ marginBottom: "0px" }}>Name: {formState.name}</h4>
                  <div>Age: {formState.age}</div>
                  <div>Location: {formState.location}</div>
                </div>
              </div>
            );
          };
          
          export default ReactFormControlledComponent;
          
==================================================================================================
Uncontrolled Component
==================================================================================================
    
    - Define an uncontrolled react form function component.
        
        .. code-block:: tsx
          :caption: src/ReactFormUncontrolledComponent.tsx
          :linenos:
          
          import React, { useRef } from "react";
          import "./App.css";
          
          const ReactFormUncontrolledComponent: React.FC = () => {
            const labelNameRef = useRef<HTMLSpanElement>(null);
            const labelAgeRef = useRef<HTMLSpanElement>(null);
            const labelLocationRef = useRef<HTMLSpanElement>(null);
          
            const labelStyle = {
              display: "inline-block",
              width: "2.5rem",
              marginRight: "1.5rem",
            };
            const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
              e.preventDefault();
              alert(
                JSON.stringify({
                  name: labelNameRef.current?.innerText,
                  age: labelAgeRef.current?.innerText,
                  location: labelLocationRef.current?.innerText,
                }),
              );
            };
          
            const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
              const { name, value } = e.target;
              if (name === "name" && labelNameRef.current) {
                labelNameRef.current.innerText = value;
              } else if (name === "age" && labelAgeRef.current) {
                labelAgeRef.current.innerText = value;
              } else if (name === "location" && labelLocationRef.current) {
                labelLocationRef.current.innerText = value;
              }
            };
          
            return (
              <div>
                <div className="App">
                  <form onSubmit={handleSubmit}>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="name" style={labelStyle}>
                        Name
                      </label>
                      <input
                        type="text"
                        id="name"
                        name="name"
                        placeholder="Enter name"
                        onChange={handleChange}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="age" style={labelStyle}>
                        Age
                      </label>
                      <input
                        type="number"
                        id="age"
                        name="age"
                        placeholder="Enter age"
                        onChange={handleChange}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="location" style={labelStyle}>
                        Location
                      </label>
                      <input
                        type="text"
                        id="location"
                        name="location"
                        placeholder="Enter location"
                        onChange={handleChange}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <input type="submit" value="Submit" />
                    </div>
                  </form>
                </div>
                <div>
                  <h4 style={{ marginBottom: "0px" }}>
                    Name: <span ref={labelNameRef}></span>
                  </h4>
                  <div>
                    Age: <span ref={labelAgeRef}></span>
                  </div>
                  <div>
                    Location: <span ref={labelLocationRef}></span>
                  </div>
                </div>
              </div>
            );
          };
          
          export default ReactFormUncontrolledComponent;
          
==================================================================================================
React Hook Form Component
==================================================================================================
    
    - Define a react hook form component.
        
        .. code-block::
          :caption: src/ReactHookFormComponent.tsx
          :linenos:
          
          import { useRef } from "react";
          import { useForm } from "react-hook-form";
          import "./App.css";
          
          const ReactHookFormComponent = () => {
            const { register, handleSubmit } = useForm();
          
            const labelNameRef = useRef<HTMLSpanElement>(null);
            const labelAgeRef = useRef<HTMLSpanElement>(null);
            const labelLocationRef = useRef<HTMLSpanElement>(null);
          
            const labelStyle = {
              display: "inline-block",
              width: "2.5rem",
              marginRight: "1.5rem",
            };
            const onFormSubmit = () => {
              if (
                labelNameRef.current &&
                labelAgeRef.current &&
                labelLocationRef.current
              ) {
                alert(
                  JSON.stringify({
                    name: labelNameRef.current.innerText,
                    age: labelAgeRef.current.innerText,
                    location: labelLocationRef.current.innerText,
                  }),
                );
              }
            };
          
            const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
              const name = e.target.name;
              if (name === "name") {
                if (labelNameRef.current) {
                  labelNameRef.current.innerText = e.target.value;
                }
              } else if (name === "age") {
                if (labelAgeRef.current) {
                  labelAgeRef.current.innerText = e.target.value;
                }
              } else if (name === "location") {
                if (labelLocationRef.current) {
                  labelLocationRef.current.innerText = e.target.value;
                }
              }
            };
          
            return (
              <div>
                <div className="App">
                  <form
                    onSubmit={(e) => {
                      e.preventDefault();
                      handleSubmit(onFormSubmit)().catch((error) => {
                        console.error("Form submission error:", error);
                      });
                    }}
                  >
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="name" style={labelStyle}>
                        Name
                      </label>
                      <input
                        type="text"
                        id="name"
                        placeholder="Enter name"
                        {...register("name")}
                        onChange={handleChange}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="age" style={labelStyle}>
                        Age
                      </label>
                      <input
                        type="number"
                        id="age"
                        placeholder="Enter age"
                        {...register("age")}
                        onChange={handleChange}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="location" style={labelStyle}>
                        Location
                      </label>
                      <input
                        type="text"
                        id="location"
                        placeholder="Enter location"
                        {...register("location")}
                        onChange={handleChange}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <input type="submit" value="Submit" />
                    </div>
                  </form>
                </div>
                <div>
                  <h4 style={{ marginBottom: "0px" }}>
                    Name: <span ref={labelNameRef}></span>
                  </h4>
                  <div>
                    Age: <span ref={labelAgeRef}></span>
                  </div>
                  <div>
                    Location: <span ref={labelLocationRef}></span>
                  </div>
                </div>
              </div>
            );
          };
          
          export default ReactHookFormComponent;
          
==================================================================================================
React Hook Form Validation
==================================================================================================
    
    - Define a react hook form component with inputs validation.
        
        .. code-block::
          :caption: src/ReactHookFormInputsValidation.tsx
          :linenos:
          
          import { useRef } from "react";
          import { useForm } from "react-hook-form";
          import "./App.css";
          
          const ReactHookFormInputsValidation = () => {
            const {
              register,
              handleSubmit,
              formState: { errors },
              reset,
            } = useForm({
              mode: "all",
            });
          
            const labelNameRef = useRef<HTMLSpanElement>(null);
            const labelAgeRef = useRef<HTMLSpanElement>(null);
            const labelLocationRef = useRef<HTMLSpanElement>(null);
          
            const labelStyle = {
              display: "inline-block",
              width: "2.5rem",
              marginRight: "1.5rem",
            };
            const onFormSubmit = () => {
              if (
                labelNameRef.current &&
                labelAgeRef.current &&
                labelLocationRef.current
              ) {
                alert(
                  JSON.stringify({
                    name: labelNameRef.current.innerText,
                    age: labelAgeRef.current.innerText,
                    location: labelLocationRef.current.innerText,
                  }),
                );
              }
              reset();
            };
          
            const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
              const name = e.target.name;
              if (name === "name") {
                if (labelNameRef.current) {
                  labelNameRef.current.innerText = e.target.value;
                }
              } else if (name === "age") {
                if (labelAgeRef.current) {
                  labelAgeRef.current.innerText = e.target.value;
                }
              } else if (name === "location") {
                if (labelLocationRef.current) {
                  labelLocationRef.current.innerText = e.target.value;
                }
              }
            };
          
            return (
              <div>
                <div className="App">
                  <form
                    noValidate
                    onSubmit={(e) => {
                      e.preventDefault();
                      handleSubmit(onFormSubmit)().catch((error) => {
                        console.error("Form submission error:", error);
                      });
                    }}
                  >
                    <div style={{ marginTop: 10 }} className="form-group">
                      <label htmlFor="name" style={labelStyle}>
                        Name
                      </label>
                      <input
                        type="text"
                        id="name"
                        placeholder="Enter name"
                        {...register("name", {
                          required: "You must enter a name",
                          minLength: {
                            value: 4,
                            message: "Name must be at least 4 characters",
                          },
                          maxLength: {
                            value: 128,
                            message: "Name must be at most 128 characters",
                          },
                        })}
                        onChange={handleChange}
                      />
                      {/*<p><ErrorMessage errors={errors} name="name" /></div>*/}
                      {errors.name && typeof errors.name.message === "string" && (
                        <div className="red-color">{errors.name.message}</div>
                      )}
                    </div>
                    <div style={{ marginTop: 10 }} className="form-group">
                      <label htmlFor="age" style={labelStyle}>
                        Age
                      </label>
                      <input
                        type="number"
                        id="age"
                        placeholder="Enter age"
                        {...register("age", {
                          valueAsNumber: true,
                          min: { value: 1, message: "Age must be at least 1 years old" },
                          max: {
                            value: 150,
                            message: "Age must be at most 150 years old",
                          },
                        })}
                        onChange={handleChange}
                      />
                      {errors.age && typeof errors.age.message === "string" && (
                        <div className="red-color">{errors.age.message}</div>
                      )}
                    </div>
                    <div style={{ marginTop: 10 }} className="form-group">
                      <label htmlFor="location" style={labelStyle}>
                        Location
                      </label>
                      <input
                        type="text"
                        id="location"
                        placeholder="Enter location"
                        {...register("location", {
                          required: "You must enter a location",
                          minLength: {
                            value: 2,
                            message: "Location must be at least 2 characters",
                          },
                          maxLength: {
                            value: 128,
                            message: "Location must be at most 128 characters",
                          },
                        })}
                        onChange={handleChange}
                      />
                      {errors.location && typeof errors.location.message === "string" && (
                        <div className="red-color">{errors.location.message}</div>
                      )}
                    </div>
                    <div style={{ marginTop: 10 }} className="form-group">
                      <input type="submit" value="Submit" />
                    </div>
                  </form>
                </div>
                <div>
                  <h4 style={{ marginBottom: "0px" }}>
                    Name: <span ref={labelNameRef}></span>
                  </h4>
                  <div>
                    Age: <span ref={labelAgeRef}></span>
                  </div>
                  <div>
                    Location: <span ref={labelLocationRef}></span>
                  </div>
                </div>
              </div>
            );
          };
          
          export default ReactHookFormInputsValidation;
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import "./list-style.css";
          import ReactHookFormInputsValidation from "./ReactHookFormInputsValidation";
          import ReactFormControlledComponent from "./ReactFormControlledComponent";
          import ReactFormUncontrolledComponent from "./ReactFormUncontrolledComponent";
          import ReactHookFormComponent from "./ReactHookFormComponent";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>React RESTful API</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Controlled Component</h3>
                      <div>
                        <ReactFormControlledComponent />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Uncontrolled Component</h3>
                      <div>
                        <ReactFormUncontrolledComponent />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>The useForm Library</h3>
                      <div>
                        <ReactHookFormComponent />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>useForm with Validation</h3>
                      <div>
                        <ReactHookFormInputsValidation />
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
        - set base to ``/react-projects/react-projects-with-typescript/tut07-react-restapi/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut07-react-restapi/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut07-react-restapi/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut07-react-restapi/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut07-react-restapi/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut07-react-restapi
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut07-react-restapi/
    - Screenshot
        
        .. figure:: images/tut06/tut06-react-form.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React RESTful APIs
           
           :custom-color-primary-bold:`React RESTful APIs`
           
