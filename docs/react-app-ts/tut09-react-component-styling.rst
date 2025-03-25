.. _tut09-react-component-styling:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Component Styling
##################################################################################################

In general, React allows component to be styled using CSS class through className attribute. Since, the React JSX supports JavaScript expression, a lot of common CSS methodology can be used.

In React, there are several ways to style components, including traditional CSS, inline styles, CSS Modules, styled-components, and Emotion.
    
    - Traditional plain CSS − regular CSS files for styling.
    - Inline Styles − CSS styles as JavaScript objects to the style attribute. The keys of the object are camelCase CSS properties, and the values are strings.
    - CSS Modules − write CSS that is scoped locally to the component, avoiding global style clashes
    - Styled-components (CSS-in-JS) − Styled-components is a popular CSS-in-JS library allowing to define styled components using JavaScript. Performance might be an issue in large apps due to runtime styling
    - Emotion (CSS-in-JS) - Emotion is another popular CSS-in-JS library similar to styled-components. It provides powerful styling capabilities, like the ability to style with JavaScript objects or template literals. Slightly more verbose syntax than styled-components.
    - Sass stylesheet − Supports Sass based CSS styles by converting the styles to normal css at build time.
    - Tailwind CSS - Tailwind provides a large set of low-level utility classes that can apply directly to HTML elements to achieve the desired design without needing to write CSS. Tailwind CSS has become very popular due to its flexibility, speed, and the ability to apply styles directly to HTML/JSX elements without writing custom CSS.
    
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut09-react-component-styling --template react-ts
        
    - Move inside the ReactJS project folder <tut09-react-component-styling> ::
        
        cd tut09-react-component-styling
        
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
          
        
**************************************************************************************************
React Components with Styling
**************************************************************************************************

==================================================================================================
Traditional Plain CSS
==================================================================================================

CSS stylesheet is usual, common and time-tested methodology. Simply create a CSS stylesheet for a component and enter all your styles for that particular component. Then, in the component, use className to refer the styles.

    
    - Add a CSS file called ``list-style.css`` in the src folder: 
        
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
          
    - Define a component using the regular plain CSS file ``list-style.css``. 
        
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
Inline Styling
==================================================================================================

Inline Styling is one of the safest ways to style the React component. It declares all the styles as JavaScript objects using DOM based css properties and set it to the component through style attributes.

Declare a variable of type object and set the styles. All css properties can be used by representing it in camelCase format. Set style in the component using curly braces {}. Also, style can be directly set inside the component

    
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
CSS Modules
==================================================================================================

Css Modules provides safest as well as easiest way to define the style. It uses normal css stylesheet with normal syntax ending with .module.css. While importing the styles, CSS modules converts all the styles into locally scoped styles so that the name conflicts will not happen. 

Create a new stylesheet ending with .module.css and write regular css styles. Here, file naming convention is very important. React toolchain will pre-process the css files ending with .module.css through CSS Module.

A CSS module file is imported into a React component file, and  a variable is defined to hold CSS class name mapping information ::
    
    import styles from './styles.module.css';
    
In the preceding code snippet, the CSS class name information is imported into a variable called styles, but the variable name can be anything we choose. The CSS class name mapping information variable is an object containing property names corresponding to the CSS class names. Each class name property contains a value of a scoped class name to be used on a React component. 

Styles within a CSS module are referenced in a component’s className attribute as follows: ::
    
    <span className={styles.error}>A bad error</span>
    <div className={`${styles.container} ${styles[type]}`}>
    className={styles.headerIcon}
    

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
Tailwind CSS
==================================================================================================

Tailwind CSS is a utility-first CSS framework that allows you to build custom designs directly in your HTML (or JSX/TSX in React) by composing utility classes. Instead of writing custom CSS, you use predefined classes to style your components, which leads to a highly customizable and maintainable design system. Tailwind CSS has become very popular due to its flexibility, speed, and the ability to apply styles directly to HTML/JSX elements without writing custom CSS.

Key Concepts of Tailwind CSS:
    
    - Utility-first: Tailwind provides a large set of low-level utility classes that you can apply directly to your HTML elements to achieve the desired design without needing to write CSS.
    - Customizability: Tailwind allows you to configure and extend your design system using the tailwind.config.js file.
    - Responsive Design: Tailwind includes built-in support for responsive design, allowing you to apply different styles based on the screen size using simple class names.
    - No custom CSS required: You can create fully styled components without writing any traditional CSS.
    


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
        - set base to ``/react-projects/react-projects-with-typescript/tut09-react-component-styling/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut09-react-component-styling/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut09-react-component-styling/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut09-react-component-styling/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut09-react-component-styling/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut09-react-component-styling
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut09-react-component-styling/
    - Screenshot
        
        .. figure:: images/tut06/tut06-react-form.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Forms
           
           :custom-color-primary-bold:`React Forms`
           
