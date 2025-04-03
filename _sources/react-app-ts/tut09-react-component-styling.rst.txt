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
        
    - Install Tailwind CSS dependencies ::
        
        # Install
        yarn add --dev tailwindcss @tailwindcss/vite
        
    - Configure the Vite plugin (edit vite.config.ts): Add the @tailwindcss/vite plugin to Vite configuration. ::
        
        // vite.config.ts
        import { defineConfig } from 'vite'
        import tailwindcss from '@tailwindcss/vite'
        export default defineConfig({
          plugins: [tailwindcss()],
        })
        
    - Add Tailwind Directives to CSS Styles. Create a new CSS file (e.g., src/index.css or src/tailwind.css) and add the Tailwind CSS directives ::
        
        /* src/tailwind.css */
        @import "tailwindcss";
        
    -  Import the CSS File into the React component. ::
        
        import './tailwind.css';  // Import the CSS file here
        
        
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
          :caption: src/ComponentUsingPlainCSS.tsx
          :linenos:
          
          import "./list-style.css";
          
          const ComponentUsingPlainCSS = () => {
            return (
              <div className="App">
                <h4 className="blue-color"> Using Plain CSS File</h4>
                <div>
                  <div className="red-color bg-blue">Blue background with red text</div>
                </div>
              </div>
            );
          };
          
          export default ComponentUsingPlainCSS;
          
==================================================================================================
Inline Styling
==================================================================================================

Inline Styling is one of the safest ways to style the React component. It declares all the styles as JavaScript objects using DOM based css properties and set it to the component through style attributes.

Declare a variable of type object and set the styles. All css properties can be used by representing it in camelCase format. Set style in the component using curly braces {}. Also, style can be directly set inside the component

    
    - Define a component using inline styles. 
        
        .. code-block:: tsx
          :caption: src/ComponentUsingInlineStyle.tsx
          :linenos:
          
          const ComponentUsingInlineStyle = () => {
            const styleObject = { backgroundColor: "blue", color: "red" };
            return (
              <div className="App">
                <h4 style={{ marginTop: "0px", marginBottom: "20px", color: "blue" }}>
                  Using Inline Style
                </h4>
                <div>
                  <div style={styleObject}>Blue background with red text</div>
                </div>
              </div>
            );
          };
          
          export default ComponentUsingInlineStyle;
          
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
    

React components:
    
    - Define a CSS module file ``custom-style.module.css``. 
        
        .. code-block:: css
          :caption: src/custom-style.module.css
          :linenos:
          
          
          .redColor {
            color:red;
          }
          
          .blueColor {
            color:blue;
          }
          .bgBlue {
            background-color: blue;
          }
          
          .margin-top-0 {
            margin-top: 0px;
          }
          
          .margin-bottom-20 {
            margin-bottom: 20px;
          }
          
    
    - Define a component using CSS modules. 
        
        .. code-block:: tsx
          :caption: src/ComponentUsingCSSModules.tsx
          :linenos:
          
          import styles from "./custom-style.module.css";
          
          const ComponentUsingCSSModules = () => {
            return (
              <div className="App">
                <h4
                  className={`${styles.blueColor} ${styles["margin-top-0"]} ${styles["margin-bottom-20"]}`}
                >
                  Using CSS Modules
                </h4>
                <div>
                  <div className={`${styles.bgBlue} ${styles.redColor}`}>
                    Blue background with red text
                  </div>
                </div>
              </div>
            );
          };
          
          export default ComponentUsingCSSModules;
          
==================================================================================================
Tailwind CSS
==================================================================================================

Tailwind CSS is a utility-first CSS framework that allows you to build custom designs directly in your HTML (or JSX/TSX in React) by composing utility classes. Instead of writing custom CSS, you use predefined classes to style your components, which leads to a highly customizable and maintainable design system. Tailwind CSS has become very popular due to its flexibility, speed, and the ability to apply styles directly to HTML/JSX elements without writing custom CSS.

Key Concepts of Tailwind CSS:
    
    - Utility-first: Tailwind provides a large set of low-level utility classes that you can apply directly to your HTML elements to achieve the desired design without needing to write CSS.
    - Customizability: Tailwind allows you to configure and extend your design system using the tailwind.config.js file.
    - Responsive Design: Tailwind includes built-in support for responsive design, allowing you to apply different styles based on the screen size using simple class names.
    - No custom CSS required: You can create fully styled components without writing any traditional CSS.
    
Steps to Set Up Tailwind CSS with Yarn:
    
    - Install Tailwind CSS dependencies ::
        
        # Install
        yarn add --dev tailwindcss @tailwindcss/vite
        
    - Configure the Vite plugin (edit vite.config.ts): Add the @tailwindcss/vite plugin to Vite configuration. ::
        
        // vite.config.ts
        import { defineConfig } from 'vite'
        import tailwindcss from '@tailwindcss/vite'
        export default defineConfig({
          plugins: [tailwindcss()],
        })
        
    - Add Tailwind Directives to CSS Styles. Create a new CSS file (e.g., src/index.css or src/tailwind.css) and add the Tailwind CSS directives ::
        
        /* src/tailwind.css */
        @import "tailwindcss";
        
    -  Import the CSS File into the React component. ::
        
        import './tailwind.css';  // Import the CSS file here
        
React components:
    
    - Define a component using Tailwind CSS 
        
        .. code-block:: tsx
          :caption: src/ComponentUsingTailwindCSS.tsx
          :linenos:
          
          import "./tailwind.css";
          
          const ComponentUsingTailwindCSS = () => {
            return (
              <div className="App">
                <div className="text-sm font-bold underline text-blue-600 mb-4">
                  Using Tailwind CSS
                </div>
                <div>
                  <div className="text-green-900 bg-blue-300">
                    Blue background with green text
                  </div>
                </div>
              </div>
            );
          };
          
          export default ComponentUsingTailwindCSS;
          
==================================================================================================
Using SVG
==================================================================================================

SVG stands for Scalable Vector Graphics and it is made up of points, lines, curves, and shapes based on mathematical formulas rather than specific pixels. This allows them to scale when resized without distortion. The quality of icons is important to get right – if they are distorted, they make the whole app feel unprofessional. Using SVGs for icons is common in modern web development.

Steps to Set Up SVG support with Yarn:
    
    - Install dependencies ::
        
        # Install
        yarn add -D vite-plugin-svgr
        
    - Configure the Vite plugin (edit vite.config.ts): Add the vite-plugin-svgr plugin to Vite configuration. ::
        
        // vite.config.ts
        import svgr from "vite-plugin-svgr";
        export default defineConfig({
          plugins: [svgr()],
        })
        
    - Configure TypeScript type inference by adding the following to ``vite-env.d.ts``: ::
        
        /// <reference types="vite-plugin-svgr/client" />
        
    -  Import SVG files as React components ::
        
        import Logo from "./logo.svg?react";
        
    - Usage:
        
        - Use with <img  />tag: <img src={svg-file} /> ::
            
            # import as a path to the SVG file, which is then used on the src attribute on the img element to display the SVG.
            import logo from './logo.svg';
            <img src={logo} className="App-logo" alt="logo" />
            
        - Import SVG files as React components ::
            
            # referencing SVG as a component
            import Logo from "./logo.svg?react";
            <div>
                <Logo />
            </div>
            
React Components
    
    - Define a component using SVG 
        
        .. code-block:: tsx
          :caption: src/ComponentUsingTailwindCSS.tsx
          :linenos:
          
          import "./tailwind.css";
          import logo from "./assets/react.svg";
          import ViteLogo from "../public/vite.svg?react";
          
          const ComponentUsingSVG = () => {
            return (
              <div className="App">
                <div className="text-sm font-bold underline text-blue-600 mb-1 mt-4">
                  As {`<img />`} Element
                </div>
                <div className="flex justify-center">
                  <img src={logo} className="App-logo" alt="logo" />
                </div>
          
                <div className="text-sm font-bold underline text-blue-600 mb-1 mt-4">
                  As ReactComponent {`<SvgComponent />`}
                </div>
                <div className="flex justify-center">
                  <ViteLogo />
                </div>
              </div>
            );
          };
          
          export default ComponentUsingSVG;
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    - Create a function component to show the user interface
        
        .. code-block:: tsx
          :caption: src/FunctionComponentsDisplay.tsx
          :linenos:
          
          import ComponentUsingCSSModules from "./ComponentUsingCSSModules";
          import ComponentUsingInlineStyle from "./ComponentUsingInlineStyle";
          import ComponentUsingPlainCSS from "./ComponentUsingPlainCSS";
          import ComponentUsingSVG from "./ComponentUsingSVG";
          import ComponentUsingTailwindCSS from "./ComponentUsingTailwindCSS";
          import "./list-style.css";
          
          const FunctionComponentsDisplay = () => {
            return (
              <div className="list-container">
                <h2>React Component Styling</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Plain CSS</h3>
                      <div>
                        <ComponentUsingPlainCSS />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Inline Styling</h3>
                      <div>
                        <ComponentUsingInlineStyle />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>CSS Modules</h3>
                      <div>
                        <ComponentUsingCSSModules />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Tailwind CSS in React</h3>
                      <div>
                        <ComponentUsingTailwindCSS />
                      </div>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Using SVG</h3>
                      <div>
                        <ComponentUsingSVG />
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
        
        .. figure:: images/tut09/tut09-react-component-styling.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Component Styling
           
           :custom-color-primary-bold:`React Component Styling`
           
