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
Components for Data Display
==================================================================================================
    
    - Define a function component for displaying each phone data.
        
        .. code-block:: tsx
          :caption: src/ComponentPhone.tsx
          :linenos:
          
          const ComponentPhone = ({
            id = "-1",
            name = "Unknown Name",
            capacity = "Unknown",
            price = "Unknown",
          }: {
            id: string;
            name: string;
            capacity: string;
            price: string;
          }) => {
            const labelStyle = {
              display: "inline-block",
              width: "3rem",
              marginRight: "1.5rem",
            };
            const itemStyle = {
              display: "inline-block",
              width: "8rem",
              marginRight: "1.5rem",
            };
            return (
              <div
                style={{ marginTop: 10, textAlign: "left", marginLeft: "40px" }}
                className="form-group"
              >
                <div>
                  <label style={labelStyle}>ID:</label>
                  <span style={itemStyle} className="blue-color">
                    {id}
                  </span>
                </div>
                <div>
                  <label style={labelStyle}>Name:</label>
                  <span style={itemStyle}>{name}</span>
                </div>
                <div>
                  <label style={labelStyle}>Capacity:</label>
                  <span style={itemStyle}>{capacity}</span>
                </div>
                <div>
                  <label style={labelStyle}>Price:</label>
                  <span style={itemStyle}>{price}</span>
                </div>
              </div>
            );
          };
          
          export default ComponentPhone;
          
    - Define a function component for displaying each people data.
        
        .. code-block:: tsx
          :caption: src/ComponentPeople.tsx
          :linenos:
          
          const ComponentPeople = ({
            id = -1,
            firstName = "Unknown Name",
            lastName = "Unknown",
            age = -1,
          }: {
            id: number;
            firstName: string;
            lastName: string;
            age: number;
          }) => {
            const labelStyle = {
              display: "inline-block",
              width: "6rem",
            };
            const itemStyle = {
              display: "inline-block",
              width: "20rem",
            };
            return (
              <div
                style={{ marginTop: 10, textAlign: "left", marginLeft: "40px" }}
                className="form-group"
              >
                <div>
                  <label style={labelStyle}>ID:</label>
                  <span style={itemStyle} className="blue-color">
                    {id}
                  </span>
                </div>
                <div>
                  <label style={labelStyle}>First Name:</label>
                  <span style={itemStyle}>{firstName}</span>
                </div>
                <div>
                  <label style={labelStyle}>Last Name:</label>
                  <span style={itemStyle}>{lastName}</span>
                </div>
                <div>
                  <label style={labelStyle}>Age:</label>
                  <span style={itemStyle}>{age}</span>
                </div>
              </div>
            );
          };
          
          export default ComponentPeople;
          

==================================================================================================
Components for Handling Data Inputs
==================================================================================================
    
    - Define a function component for adding new phone data.
        
        .. code-block::
          :caption: src/FormComponentPhone.tsx
          :linenos:
          
          import { useForm } from "react-hook-form";
          import "./App.css";
          
          interface FormComponentPhoneProps {
            serverError: boolean;
            addPhone: ({
              name,
              capacity,
              price,
            }: {
              name: string;
              capacity: string;
              price: string;
            }) => Promise<void>;
          }
          interface FormData {
            name: string;
            capacity: string;
            price: string;
          }
          
          const FormComponentPhone: React.FC<FormComponentPhoneProps> = (props) => {
            const { serverError, addPhone } = { ...props };
            const { register, handleSubmit, reset } = useForm<FormData>();
          
            const labelStyle = {
              display: "inline-block",
              width: "3rem",
              marginRight: "1.5rem",
            };
          
            return (
              <div>
                <div className="App">
                  <form
                    onSubmit={(e) => {
                      e.preventDefault();
                      void handleSubmit(addPhone)();
                      reset();
                    }}
                  >
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="name" style={labelStyle}>
                        Name:
                      </label>
                      <input
                        type="text"
                        placeholder="Enter phone name"
                        {...register("name")}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="capacity" style={labelStyle}>
                        Capacity:
                      </label>
                      <input
                        type="text"
                        placeholder="Enter phone capacity"
                        {...register("capacity")}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="price" style={labelStyle}>
                        Price:
                      </label>
                      <input
                        type="text"
                        placeholder="Enter price"
                        {...register("price")}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <input type="submit" value="Submit" disabled={serverError} />
                    </div>
                  </form>
                </div>
              </div>
            );
          };
          export default FormComponentPhone;
          
          
    - Define a function component for adding new people data.
        
        .. code-block::
          :caption: src/FormComponentPeople.tsx
          :linenos:
          
          import { useForm } from "react-hook-form";
          import "./App.css";
          
          interface FormComponentPeopleProps {
            serverError: boolean;
            addPeople: ({
              firstName,
              lastName,
              age,
            }: {
              firstName: string;
              lastName: string;
              age: number;
            }) => Promise<void>;
          }
          interface FormData {
            firstName: string;
            lastName: string;
            age: number;
          }
          
          const FormComponentPeople: React.FC<FormComponentPeopleProps> = (props) => {
            const { serverError, addPeople } = { ...props };
            const { register, handleSubmit, reset } = useForm<FormData>();
          
            const labelStyle = {
              display: "inline-block",
              width: "6rem",
              marginRight: "1.5rem",
            };
          
            return (
              <div>
                <div className="App">
                  <form
                    onSubmit={(e) => {
                      e.preventDefault();
                      void handleSubmit(addPeople)();
                      reset();
                    }}
                  >
                    <div style={{ marginTop: 20 }}>
                      <label htmlFor="firstName" style={labelStyle}>
                        First Name:
                      </label>
                      <input
                        type="text"
                        placeholder="Enter first name"
                        {...register("firstName")}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="lastName" style={labelStyle}>
                        Last Name:
                      </label>
                      <input
                        type="text"
                        placeholder="Enter last name"
                        {...register("lastName")}
                      />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <label htmlFor="age" style={labelStyle}>
                        Age:
                      </label>
                      <input type="number" placeholder="Enter age" {...register("age")} />
                    </div>
                    <div style={{ marginTop: 10 }}>
                      <input type="submit" value="Submit" disabled={serverError} />
                    </div>
                  </form>
                </div>
              </div>
            );
          };
          export default FormComponentPeople;
          
          
==================================================================================================
Using Fetch
==================================================================================================
    
--------------------------------------------------------------------------------------------------
Fetch: Getting Data List
--------------------------------------------------------------------------------------------------
    
    - Define a function component using fetch to get phones and peoples from two public servers.
        
        .. code-block::
          :caption: src/FetchGetComponent.tsx
          :linenos:
          
          import React, { useState, useEffect, useRef } from "react";
          import ComponentPhone from "./ComponentPhone";
          import ComponentPeople from "./ComponentPeople";
          import "./App.css";
          
          interface Phone {
            id: string;
            name: string;
            data: {
              Capacity: string;
              Price: string;
            };
          }
          interface People {
            id: number;
            firstName: string;
            lastName: string;
            age: number;
          }
          const FetchGetComponent: React.FC = () => {
            const [phones, setPhones] = useState<Phone[]>([]);
            const [isPhonesLoading, setPhonesLoading] = useState(true);
          
            const [peoples, setPeoples] = useState<People[]>([]);
            const [isPeoplesLoading, setPeoplesLoading] = useState(true);
          
            const getPhoneError = useRef<HTMLDivElement>(null);
            const getPeopleError = useRef<HTMLDivElement>(null);
          
            useEffect(() => {
              const fetchPhones = async () => {
                await fetch("https://api.restful-api.dev/objects?id=12&id=13")
                  .then((response) => {
                    if (response.ok) {
                      return response.json() as unknown as Phone[];
                    }
                    throw new Error(`Failed to fetch data, Status: ${response.status}`);
                  })
                  .then((data) => {
                    //console.log(data);
                    setPhones(data);
                    setPhonesLoading(false);
                  })
                  .catch((err) => {
                    if (err instanceof Error) {
                      //console.log(err.message); // Error message  output
                      if (getPhoneError.current) {
                        getPhoneError.current.textContent = err.message;
                      }
                    }
                    setPhonesLoading(true);
                  });
              };
              const fetchPeoples = async () => {
                await fetch("https://softwium.com/api/peoples?limit=2")
                  .then((response) => {
                    if (response.ok) {
                      return response.json() as unknown as People[];
                    }
                    throw new Error(`Failed to fetch data, Status: ${response.status}`);
                  })
                  .then((data) => {
                    //console.log(data);
                    setPeoples(data);
                    setPeoplesLoading(false);
                  })
                  .catch((err) => {
                    if (err instanceof Error) {
                      //console.log(err.message); // Error message  output
                      if (getPeopleError.current) {
                        getPeopleError.current.textContent = err.message;
                      }
                    }
                    setPeoplesLoading(true);
                  });
              };
              void fetchPhones();
              void fetchPeoples();
            }, []);
            return (
              <>
                <div style={{ marginTop: "20px" }}>
                  <h3>Fetch Two Phone Objects</h3>
                  <h5 className="blue-color" style={{ marginTop: "0px" }}>
                    Server: https://api.restful-api.dev/objects
                  </h5>
                  <div>
                    <h4>Phone List</h4>
                    {isPhonesLoading && (
                      <div>
                        <div>Loading...</div>
                        <div className="red-color" ref={getPhoneError}></div>
                      </div>
                    )}
                    <div>
                      {phones.length > 0 &&
                        phones.map((phone) => {
                          return (
                            <div key={phone.id} style={{ marginTop: "10px" }}>
                              <ComponentPhone
                                id={phone.id}
                                name={phone.name}
                                capacity={phone.data.Capacity}
                                price={phone.data.Price}
                              />
                            </div>
                          );
                        })}
                    </div>
                  </div>
                </div>
                <div style={{ marginTop: "20px" }}>
                  <h3>Fetch Two Peoples</h3>
                  <h5 className="blue-color" style={{ marginTop: "0px" }}>
                    Server: https://softwium.com/api/peoples
                  </h5>
                  <div>
                    <h4>People List</h4>
                    {isPeoplesLoading && (
                      <div>
                        <div>Loading...</div>
                        <div className="red-color" ref={getPeopleError}></div>
                      </div>
                    )}
                    <div>
                      {peoples.length > 0 &&
                        peoples.map((people) => {
                          return (
                            <div key={people.id} style={{ marginTop: "10px" }}>
                              <ComponentPeople
                                id={people.id}
                                firstName={people.firstName}
                                lastName={people.lastName}
                                age={people.age}
                              />
                            </div>
                          );
                        })}
                    </div>
                  </div>
                </div>
              </>
            );
          };
          
          export default FetchGetComponent;
          
--------------------------------------------------------------------------------------------------
Fetch: Adding Data
--------------------------------------------------------------------------------------------------
    
    - Define a function component using fetch to add new phone and people from two public servers.
        
        .. code-block::
          :caption: src/FetchPostComponent.tsx
          :linenos:
          
          import React, { useState, useEffect, useRef } from "react";
          import FormComponentPhone from "./FormComponentPhone";
          import ComponentPhone from "./ComponentPhone";
          import ComponentPeople from "./ComponentPeople";
          import FormComponentPeople from "./FormComponentPeople";
          import "./App.css";
          
          interface Phone {
            id: string;
            name: string;
            data: {
              Capacity: string;
              Price: string;
            };
          }
          interface People {
            id: number;
            firstName: string;
            lastName: string;
            age: number;
          }
          const FetchPostComponent: React.FC = () => {
            const [phones, setPhones] = useState<Phone[]>([]);
            const [isPhonesLoading, setPhonesLoading] = useState(true);
            const [isPhonesServerError, setPhonesServerError] = useState(false);
            const [peoples, setPeoples] = useState<People[]>([]);
            const [isPeoplesLoading, setPeoplesLoading] = useState(true);
          
            const [isPeoplesServerError, setPeoplesServerError] = useState(false);
            const getPhoneError = useRef<HTMLDivElement>(null);
            const getPeopleError = useRef<HTMLDivElement>(null);
          
            useEffect(() => {
              const fetchPhones = async () => {
                await fetch("https://api.restful-api.dev/objects?id=12&id=13")
                  .then((response) => {
                    if (response.ok) {
                      return response.json() as unknown as Phone[];
                    }
                    throw new Error(`Failed to fetch data, Status: ${response.status}`);
                  })
                  .then((data) => {
                    //console.log(data);
                    setPhones(data);
                    setPhonesLoading(false);
                  })
                  .catch((err) => {
                    if (err instanceof Error) {
                      //console.log(err.message); // Error message  output
                      if (getPhoneError.current) {
                        getPhoneError.current.textContent = err.message;
                      }
                    }
                    setPhonesServerError(true);
                    setPhonesLoading(true);
                  });
              };
              const fetchPeoples = async () => {
                await fetch("https://softwium.com/api/peoples?limit=2")
                  .then((response) => {
                    if (response.ok) {
                      return response.json() as unknown as People[];
                    }
                    throw new Error(`Failed to fetch data, Status: ${response.status}`);
                  })
                  .then((data) => {
                    //console.log(data);
                    setPeoples(data);
                    setPeoplesLoading(false);
                  })
                  .catch((err) => {
                    if (err instanceof Error) {
                      //console.log(err.message); // Error message  output
                      if (getPeopleError.current) {
                        getPeopleError.current.textContent = err.message;
                      }
                    }
                    setPeoplesServerError(true);
                    setPeoplesLoading(true);
                  });
              };
              void fetchPhones();
              void fetchPeoples();
            }, []);
          
            const addPhoneItem = async ({
              name,
              capacity,
              price,
            }: {
              name: string;
              capacity: string;
              price: string;
            }) => {
              await fetch("https://api.restful-api.dev/objects", {
                method: "POST",
                body: JSON.stringify({
                  name: name,
                  data: {
                    Capacity: capacity,
                    Price: price,
                  },
                }),
                headers: {
                  "Content-type": "application/json; charset=UTF-8",
                },
              })
                .then((response) => response.json() as unknown as Phone)
                .then((data) => {
                  setPhones((phones) => [...phones, data]);
                  setPhonesLoading(false);
                })
                .catch((err) => {
                  if (err instanceof Error) {
                    console.log(err.message);
                  }
                  setPhonesServerError(true);
                  setPhonesLoading(true);
                });
            };
            const addPeopleItem = async ({
              firstName,
              lastName,
              age,
            }: {
              firstName: string;
              lastName: string;
              age: number;
            }) => {
              await fetch("https://api.restful-api.dev/objects", {
                method: "POST",
                body: JSON.stringify({
                  firstName: firstName,
                  lastName: lastName,
                  age: age,
                }),
                headers: {
                  "Content-type": "application/json; charset=UTF-8",
                },
              })
                .then((response) => response.json() as unknown as People)
                .then((data) => {
                  if (!data.firstName) data.firstName = firstName;
                  if (!data.lastName) data.lastName = lastName;
                  if (!data.age) data.age = age;
                  setPeoples((peoples) => [...peoples, data]);
                  setPeoplesLoading(false);
                })
                .catch((err) => {
                  if (err instanceof Error) {
                    console.log(err.message);
                  }
                  setPeoplesServerError(true);
                  setPeoplesLoading(true);
                });
            };
            return (
              <>
                <div style={{ marginTop: "20px" }}>
                  <h3>Fetch Post: Add New Phone Item</h3>
                  <h5 className="blue-color" style={{ marginTop: "0px" }}>
                    Server: https://api.restful-api.dev/objects
                  </h5>
                  <FormComponentPhone
                    serverError={isPhonesServerError}
                    addPhone={addPhoneItem}
                  />
                  <div>
                    <h4>Phone List</h4>
                    {isPhonesLoading && (
                      <div>
                        <div>Loading...</div>
                        <div className="red-color" ref={getPhoneError}></div>
                      </div>
                    )}
                    <div>
                      {phones.length > 0 &&
                        phones.map((phone) => {
                          return (
                            <div key={phone.id} style={{ marginTop: "10px" }}>
                              <ComponentPhone
                                id={phone.id}
                                name={phone.name}
                                capacity={phone.data.Capacity}
                                price={phone.data.Price}
                              />
                            </div>
                          );
                        })}
                    </div>
                  </div>
                </div>
                <div style={{ marginTop: "20px" }}>
                  <h3>Fetch Post: Add New People</h3>
                  <h5 className="blue-color" style={{ marginTop: "0px" }}>
                    Server: https://softwium.com/api/peoples
                  </h5>
                  <FormComponentPeople
                    serverError={isPeoplesServerError}
                    addPeople={addPeopleItem}
                  />
                  <div>
                    <h4>People List</h4>
                    {isPeoplesLoading && (
                      <div>
                        <div>Loading...</div>
                        <div className="red-color" ref={getPeopleError}></div>
                      </div>
                    )}
                    <div>
                      {peoples.length > 0 &&
                        peoples.map((people) => {
                          return (
                            <div key={people.id} style={{ marginTop: "10px" }}>
                              <ComponentPeople
                                id={people.id}
                                firstName={people.firstName}
                                lastName={people.lastName}
                                age={people.age}
                              />
                            </div>
                          );
                        })}
                    </div>
                  </div>
                </div>
              </>
            );
          };
          
          export default FetchPostComponent;
          
                    
==================================================================================================
Using axios Library
==================================================================================================
    
--------------------------------------------------------------------------------------------------
Axios: Getting Data List
--------------------------------------------------------------------------------------------------
    
    - Define a function component using axios to get phones and peoples from two public servers.
        
        .. code-block::
          :caption: src/AxiosGetComponent.tsx
          :linenos:
          
          import React, { useState, useEffect, useRef } from "react";
          import axios from "axios";
          import ComponentPhone from "./ComponentPhone";
          import ComponentPeople from "./ComponentPeople";
          import "./App.css";
          
          interface Phone {
            id: string;
            name: string;
            data: {
              Capacity: string;
              Price: string;
            };
          }
          interface People {
            id: number;
            firstName: string;
            lastName: string;
            age: number;
          }
          const AxiosGetComponent: React.FC = () => {
            const [phones, setPhones] = useState<Phone[]>([]);
            const [isPhonesLoading, setPhonesLoading] = useState(true);
          
            const [peoples, setPeoples] = useState<People[]>([]);
            const [isPeoplesLoading, setPeoplesLoading] = useState(true);
          
            const getPhoneError = useRef<HTMLDivElement>(null);
            const getPeopleError = useRef<HTMLDivElement>(null);
          
            useEffect(() => {
              const getPhones = async () => {
                await axios
                  .get("https://api.restful-api.dev/objects?id=12&id=13")
                  .then((response) => {
                    return response.data as JSON as unknown as Phone[];
                  })
                  .then((data) => {
                    //console.log(data);
                    setPhones(data);
                    setPhonesLoading(false);
                  })
                  .catch((err) => {
                    if (err instanceof Error) {
                      //console.log(err.message); // Error message  output
                      if (getPhoneError.current) {
                        getPhoneError.current.textContent = err.message;
                      }
                    }
                    setPhonesLoading(true);
                  });
              };
              const getPeoples = async () => {
                await axios
                  .get("https://softwium.com/api/peoples?limit=2")
                  .then((response) => response.data as JSON as unknown as People[])
                  .then((data) => {
                    //console.log(data);
                    setPeoples(data);
                    setPeoplesLoading(false);
                  })
                  .catch((err) => {
                    if (err instanceof Error) {
                      //console.log(err.message); // Error message  output
                      if (getPeopleError.current) {
                        getPeopleError.current.textContent = err.message;
                      }
                    }
                    setPeoplesLoading(true);
                  });
              };
              void getPhones();
              void getPeoples();
            }, []);
            return (
              <>
                <div style={{ marginTop: "20px" }}>
                  <h3>Axios: Get Two Phone Objects</h3>
                  <h5 className="blue-color" style={{ marginTop: "0px" }}>
                    Server: https://api.restful-api.dev/objects
                  </h5>
                  <div>
                    <h4>Phone List</h4>
                    {isPhonesLoading && (
                      <div>
                        <div>Loading...</div>
                        <div className="red-color" ref={getPhoneError}></div>
                      </div>
                    )}
                    <div>
                      {phones.length > 0 &&
                        phones.map((phone) => {
                          return (
                            <div key={phone.id} style={{ marginTop: "10px" }}>
                              <ComponentPhone
                                id={phone.id}
                                name={phone.name}
                                capacity={phone.data.Capacity}
                                price={phone.data.Price}
                              />
                            </div>
                          );
                        })}
                    </div>
                  </div>
                </div>
                <div style={{ marginTop: "20px" }}>
                  <h3>Axios: Get Two Peoples</h3>
                  <h5 className="blue-color" style={{ marginTop: "0px" }}>
                    Server: https://softwium.com/api/peoples
                  </h5>
                  <div>
                    <h4>People List</h4>
                    {isPeoplesLoading && (
                      <div>
                        <div>Loading...</div>
                        <div className="red-color" ref={getPeopleError}></div>
                      </div>
                    )}
                    <div>
                      {peoples.length > 0 &&
                        peoples.map((people) => {
                          return (
                            <div key={people.id} style={{ marginTop: "10px" }}>
                              <ComponentPeople
                                id={people.id}
                                firstName={people.firstName}
                                lastName={people.lastName}
                                age={people.age}
                              />
                            </div>
                          );
                        })}
                    </div>
                  </div>
                </div>
              </>
            );
          };
          
          export default AxiosGetComponent;
          
--------------------------------------------------------------------------------------------------
Axios: Adding Data
--------------------------------------------------------------------------------------------------
    
    - Define a function component using axios to add new phone and people from two public servers.
        
        .. code-block::
          :caption: src/AxiosPostComponent.tsx
          :linenos:
          
          import React, { useState, useEffect, useRef } from "react";
          import axios from "axios";
          import FormComponentPhone from "./FormComponentPhone";
          import ComponentPhone from "./ComponentPhone";
          import ComponentPeople from "./ComponentPeople";
          import FormComponentPeople from "./FormComponentPeople";
          import "./App.css";
          
          interface Phone {
            id: string;
            name: string;
            data: {
              Capacity: string;
              Price: string;
            };
          }
          interface People {
            id: number;
            firstName: string;
            lastName: string;
            age: number;
          }
          const AxiosPostComponent: React.FC = () => {
            const [phones, setPhones] = useState<Phone[]>([]);
            const [isPhonesLoading, setPhonesLoading] = useState(true);
            const [isPhonesServerError, setPhonesServerError] = useState(false);
            const [peoples, setPeoples] = useState<People[]>([]);
            const [isPeoplesLoading, setPeoplesLoading] = useState(true);
          
            const [isPeoplesServerError, setPeoplesServerError] = useState(false);
            const getPhoneError = useRef<HTMLDivElement>(null);
            const getPeopleError = useRef<HTMLDivElement>(null);
          
            useEffect(() => {
              const getPhones = async () => {
                await axios
                  .get("https://api.restful-api.dev/objects?id=12&id=13")
                  .then((response) => {
                    return response.data as JSON as unknown as Phone[];
                  })
                  .then((data) => {
                    //console.log(data);
                    setPhones(data);
                    setPhonesLoading(false);
                  })
                  .catch((err) => {
                    if (err instanceof Error) {
                      //console.log(err.message); // Error message  output
                      if (getPhoneError.current) {
                        getPhoneError.current.textContent = err.message;
                      }
                    }
                    setPhonesLoading(true);
                  });
              };
              const getPeoples = async () => {
                await axios
                  .get("https://softwium.com/api/peoples?limit=2")
                  .then((response) => response.data as JSON as unknown as People[])
                  .then((data) => {
                    //console.log(data);
                    setPeoples(data);
                    setPeoplesLoading(false);
                  })
                  .catch((err) => {
                    if (err instanceof Error) {
                      //console.log(err.message); // Error message  output
                      if (getPeopleError.current) {
                        getPeopleError.current.textContent = err.message;
                      }
                    }
                    setPeoplesLoading(true);
                  });
              };
              void getPhones();
              void getPeoples();
            }, []);
          
            const addPhoneItem = async ({
              name,
              capacity,
              price,
            }: {
              name: string;
              capacity: string;
              price: string;
            }) => {
              await axios
                .post("https://api.restful-api.dev/objects", {
                  name: name,
                  data: {
                    Capacity: capacity,
                    Price: price,
                  },
                })
                .then((response) => response.data as JSON as unknown as Phone)
                .then((data) => {
                  setPhones((phones) => [...phones, data]);
                  setPhonesLoading(false);
                })
                .catch((err) => {
                  if (err instanceof Error) {
                    console.log(err.message);
                  }
                  setPhonesServerError(true);
                  setPhonesLoading(true);
                });
            };
            const addPeopleItem = async ({
              firstName,
              lastName,
              age,
            }: {
              firstName: string;
              lastName: string;
              age: number;
            }) => {
              await axios
                .post("https://api.restful-api.dev/objects", {
                  firstName: firstName,
                  lastName: lastName,
                  age: age,
                })
                .then((response) => response.data as JSON as unknown as People)
                .then((data) => {
                  if (!data.firstName) data.firstName = firstName;
                  if (!data.lastName) data.lastName = lastName;
                  if (!data.age) data.age = age;
                  setPeoples((peoples) => [...peoples, data]);
                  setPeoplesLoading(false);
                })
                .catch((err) => {
                  if (err instanceof Error) {
                    console.log(err.message);
                  }
                  setPeoplesServerError(true);
                  setPeoplesLoading(true);
                });
            };
            return (
              <>
                <div style={{ marginTop: "20px" }}>
                  <h3>Axios Post: Add New Phone Item</h3>
                  <h5 className="blue-color" style={{ marginTop: "0px" }}>
                    Server: https://api.restful-api.dev/objects
                  </h5>
                  <FormComponentPhone
                    serverError={isPhonesServerError}
                    addPhone={addPhoneItem}
                  />
                  <div>
                    <h4>Phone List</h4>
                    {isPhonesLoading && (
                      <div>
                        <div>Loading...</div>
                        <div className="red-color" ref={getPhoneError}></div>
                      </div>
                    )}
                    <div>
                      {phones.length > 0 &&
                        phones.map((phone) => {
                          return (
                            <div key={phone.id} style={{ marginTop: "10px" }}>
                              <ComponentPhone
                                id={phone.id}
                                name={phone.name}
                                capacity={phone.data.Capacity}
                                price={phone.data.Price}
                              />
                            </div>
                          );
                        })}
                    </div>
                  </div>
                </div>
                <div style={{ marginTop: "20px" }}>
                  <h3>Axios Post: Add New People</h3>
                  <h5 className="blue-color" style={{ marginTop: "0px" }}>
                    Server: https://softwium.com/api/peoples
                  </h5>
                  <FormComponentPeople
                    serverError={isPeoplesServerError}
                    addPeople={addPeopleItem}
                  />
                  <div>
                    <h4>People List</h4>
                    {isPeoplesLoading && (
                      <div>
                        <div>Loading...</div>
                        <div className="red-color" ref={getPeopleError}></div>
                      </div>
                    )}
                    <div>
                      {peoples.length > 0 &&
                        peoples.map((people) => {
                          return (
                            <div key={people.id} style={{ marginTop: "10px" }}>
                              <ComponentPeople
                                id={people.id}
                                firstName={people.firstName}
                                lastName={people.lastName}
                                age={people.age}
                              />
                            </div>
                          );
                        })}
                    </div>
                  </div>
                </div>
              </>
            );
          };
          
          export default AxiosPostComponent;
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import AxiosGetComponent from "./AxiosGetComponent";
          import AxiosPostComponent from "./AxiosPostComponent";
          import FetchGetComponent from "./FetchGetComponent";
          import FetchPostComponent from "./FetchPostComponent";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>React RESTful API</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Fetch API: GET Requests</h3>
                      <div>
                        <FetchGetComponent />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Fetch API: Post Requests</h3>
                      <div>
                        <FetchPostComponent />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Axios API: GET Requests</h3>
                      <div>
                        <AxiosGetComponent />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Axios API: Post Requests</h3>
                      <div>
                        <AxiosPostComponent />
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
        
        .. figure:: images/tut07/tut07-react-restapi.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React RESTful APIs
           
           :custom-color-primary-bold:`React RESTful APIs`
           
