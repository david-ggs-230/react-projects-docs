.. _tut06-react-form:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Form
##################################################################################################

**************************************************************************************************
Introduction
**************************************************************************************************

Forms are an essential part of any application used for collecting user data, processing payments, or handling authentication. React Forms are the components used to collect and manage the user inputs. These components include the input elements like text field, check box, date input, dropdowns etc. The nature of form programming needs the state to be maintained and the input field information will get changed as the user interacts with the form.

In React, there are two ways of handling form data:
    
    - Controlled Components: In this approach, form data is handled by React through the use of hooks such as the useState hook. When a component is controlled, the value of form elements is stored in a state, and any changes made to the value are immediately reflected in the state.
        
        - To create a controlled component, you need to use the value prop to set the value of form elements and the onChange event to handle changes made to the value.
        - The value prop sets the initial value of a form element
        - The onChange event is triggered whenever the value of a form element changes.
        - Inside the onChange event, you need to update the state with the new value using a state update function.
        
    - Uncontrolled Components: In uncontrolled components, React does not manage the state of input elements and doesn’t track the value of the input fields. Form data is handled by the Document Object Model (DOM) rather than by React. The DOM maintains the state of form data and updates it based on user input. When a user enters text into a text input field or selects an option from a select box, the browser updates the DOM's state for that element automatically.
        
        - React provides a ref attribute for all its DOM element.
        - React use the useRef hook to create a new reference and then attach it to the form element.
        - When a user interacts with a form element in uncontrolled component, the browser automatically updates the DOM's state for that element. 
        - React use the attached reference to retrieve the current values of each form element during runtime.
        - Uncontrolled components can be useful in certain situations, such as when you need to integrate with third-party libraries or when you don't need to manipulate the form data.
        

==================================================================================================
Controlled Components
==================================================================================================

In controlled component, React provides a special attribute, value for all input elements and controls the input elements, and use the useState Hook to keep track of each inputs value. React control the values of more than one input field by adding a name attribute to each element.

The sample usage to set and update the user's form input is as follows ::
    
    const [inputs, setInputs] = useState({});
    
    <input 
        type="text" 
        name="fieldname" 
        value={inputs.fieldname || ""} 
        onChange={handleChange}
    />
    
    // update the state
    const handleChange = (event) => {
      const name = event.target.name;
      const value = event.target.value;
      setInputs(values => ({...values, [name]: value}))
    }
    
    // Handle form submit
    const handleSubmit = (event) => {
      event.preventDefault();
      ...
    }
    
==================================================================================================
Uncontrolled Components
==================================================================================================

In uncontrolled components, React does not manage the state of input elements and doesn't track the value of the input fields. Instead, it allows the DOM to handle the input's state. React provides a ref attribute for all its DOM element and a corresponding api, React.createRef() to create a new reference (this.ref). The newly created reference can be attached to the form element and the attached form element's value can be accessed using this.ref.current.value whenever necessary.

The sample usage to do form programming in uncontrolled component:
    
    - Step 1 − Create a reference ::
        
        this.inputRef = React.createRef();
        
    - Step 2 − Create a form element ::
        
        <input type="text" name="username" />
        
    - Step 3 − Attach the already created reference in the form element ::
        
        <input type="text" name="username" ref={this.inputRef} />
        
    - Step 4 − Get the input value using this.inputRef.current.value during validation and submission ::
        
        <div> input: {this.inputRef.current.value} </div> 
        
    
React libraries for handling forms:
    
    - React Hook Form: React Hook Form is a React library for building forms. It is very flexible and can be used for simple forms as well as large forms with complex validation and submission logic. It is also very performant and optimised not to cause unnecessary re-renders.
    - React Router Form: Form is a wrapper around the HTML form element that handles the form submission on the client side. React Router’s form submission mimics how a native form element submits to a server path. However, React Router submits the form to a client-side route instead. In addition, Form mimics an HTTP GET request by default
    - Other libraries
        

==================================================================================================
React Hook Form Library
==================================================================================================

--------------------------------------------------------------------------------------------------
React Hook Form
--------------------------------------------------------------------------------------------------

React Hook Form is a React library for building forms. It is very flexible and can be used for simple forms as well as large forms with complex validation and submission logic. It is also very performant and optimised not to cause unnecessary re-renders.
    
    - install the react-hook-form library ::
        
        # npm install the react-hook-form library 
        npm install react-hook-form
        # yarn install the react-hook-form library 
        yarn add react-hook-form
        
    - import the useForm hook from the library ::
        
        # import the useForm hook
        import { useForm } from "react-hook-form";
        
    - use the useForm hook ::
        
        # destructure the register and handleSubmit properties
        const { register, handleSubmit, formState: {errors, isSubmitting, isSubmitSuccessful} } = useForm();
        
    - register an input element ::
        
        # register an input element with a variable name. This spread operator syntax is a new implementation to 
        #    the library that enables strict type checking in forms with TypeScript. 
        <input type="text" name="firstName" {...register('firstName')} />
        # React Hook Form versions older than v7 had the register method attached to the ref attribute as such:
        #    <input type="text" name="firstName" ref={register} />
        
    - form submission. The handleSubmit method can handle two functions as arguments. The first function passed as an argument will be invoked when the form validation is successful. The second function is called with errors when the validation fails ::
        
        # create onSubmit and onErrors methods to handle form submission
        const onFormSubmit  = data => console.log(data);
        const onErrors = errors => console.error(errors);
        <form onSubmit={handleSubmit(onFormSubmit, onErrors)}>
            {/* ... */}
        </form>
        
--------------------------------------------------------------------------------------------------
React Hook Form Inputs Validation
--------------------------------------------------------------------------------------------------
    
    - The validation parameters include the following properties:
        
        - required
            indicates if the field is required or not. If this property is set to true, then the field cannot be empty
        - minlength and maxlength
            set the minimum and maximum length for a string input value
        - min and max 
            set the minimum and maximum values for a numerical value
        - type
            indicates the type of the input field; it can be email, number, text, or any other standard HTML input types
        - pattern
            defines a pattern for the input value using a regular expression
            
    - Install ErrorMessage component to handle errors if desired
        
        - install by npm 
            npm install @hookform/error-message
        - install by yarn 
            yarn add @hookform/error-message
        
    - Validate with RegisterOptions
        
        - Specifying validation
            
            - Field validation is defined in the register field in an options parameter as follows:
                
                - <input {...register('name', { required: true })} />
                - <input {...register('name', { required: 'You must enter a name' })} />
                - <input {...register('name', { required: 'You must enter a name', pattern: { value: /\S+/, message: 'Entered value does not match pattern format', } }) } />
                
            - Add a noValidate attribute to the form element to prevent any native HTML validation
                
                - <form noValidate onSubmit={handleSubmit(onSubmit)}>
                
            - Obtaining validation errors
                
                - The useForm returns a state called errors, which contains the form validation errors
                - The errors state is an object containing invalid field error messages.
                    
                    For example, if a name field is invalid because a required rule has been violated, the errors object could be as follows ::
                      
                      { name: {
                                   message: 'You must enter your name',
                                   type: 'required'
                              }
                      }
                      
            - Use the errors object to display custom error messages
                
                - { errors.name && <p className="errorMsg">{errors.name.message}</p> }
                
        - Handling submission with form validation
            
            - The isSubmitting state can be used to disable elements whilst the form is being submitted ::
                
                <button type="submit" disabled={isSubmitting}>Submit</button>
                
            - The isSubmitSuccessful can be used to conditionally render a successful submission message ::
                
                if (isSubmitSuccessful) { 
                    return <div>The form was successfully submitted</div>;
                }
                
        
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut06-react-form --template react-ts
        
    - Move inside the ReactJS project folder <tut06-react-form> ::
        
        cd tut06-react-form
        
    - Install the dependencies ::
        
        yarn install
        
    - Install the react-hook-form library dependencies ::
        
        yarn add react-hook-form
        
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
React Form Components
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
    
    - Create a function component to show the user interface
        
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
                <h2>React Form</h2>
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
        - set base to ``/react-projects/react-projects-with-typescript/tut06-react-form/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut06-react-form/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut06-react-form/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut06-react-form/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut06-react-form/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut06-react-form
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut06-react-form/
    - Screenshot
        
        .. figure:: images/tut06/tut06-react-form.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Forms
           
           :custom-color-primary-bold:`React Forms`
           
