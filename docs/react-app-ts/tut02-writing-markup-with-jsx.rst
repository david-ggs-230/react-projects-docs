.. _tut02-writing-markup-with-jsx:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Tut02-Writing Markup with JSX
##################################################################################################

**************************************************************************************************
JSX Syntax and Rules
**************************************************************************************************

JSX is a JavaScript syntax extension that allows developers to use **HTML-like** markup within their JavaScript files. JSX is short for JavaScript XML(Extensible Markup Language). 

The Rules of JSX:
    
    - Return a single root element
        
        - must wrap return elements with a single parent tag
        - It is common practice to wrap everything in a **div** or a **Fragment**. The empty JSX tag **<></>** is shorthand for <Fragment></Fragment>. 
        
    - Close all the tags
        
        - JSX requires tags to be explicitly closed
        - For instance, ``<li>`` tag must be written as ``<li> ... </li>``
        - Elements without children must be self-closed in JSX. For instance, <img> must become <img />
        - When rendering lists of elements, each item should have a unique key attribute to help React identify which items have changed, been added, or removed. 
        
    - Attributes in JSX
        
        - Attributes in JSX are similar to HTML but follow camelCase naming conventions
        - JSX turns into JavaScript and attributes written in JSX become keys of JavaScript objects
        - Attributes can’t contain dashes or be reserved words like class, and many HTML and SVG attributes used in JSX are written in camelCase
        - For instance, attributes ``class`` becomes ``className``, ``tabindex`` becomes ``tabIndex``, and  ``stroke-width`` becomes ``strokeWidth``
        - Put a string attribute in single or double quotes
        - Recommend `using a converter to translate the existing HTML and SVG to JSX <https://transform.tools/html-to-jsx>`_
        
    - Event Handling
        
        - Event handlers in JSX are written in camelCase and passed as functions. 
        - For example, onclick in HTML becomes onClick in JSX.
        
    - Embedding JavaScript Expressions
        
        - Embedding JavaScript expressions within curly braces {}
        - { variable }
        - { functioncall() }
        - Embedding JavaScript expressions as text directly inside a JSX tag, eg: <h1>{name}'s To Do List</h1>
        - Embedding JavaScript expressions as attributes immediately following the = sign, eg: src={avatar}
        
    - Embedding JavaScript Objects and CSS
        
        - Embedding JavaScript and CSS objects within double curlies {{ }}
        - Embedding JavaScript object in JSX, eg: person={{ name: "Hedy Lamarr", inventions: 5 }}
        - Embedding inline CSS styles in JSX, eg: <ul style={{ backgroundColor: 'black', color: 'pink' }}> ... </ul>
        - Note: properties of JavaScript and CSS objects are written in camelCase. For example, <ul style={{ backgroundColor: 'black' }}>
        

**************************************************************************************************
Rendering with JSX
**************************************************************************************************

==================================================================================================
Create a ReactJS Project with Vite
==================================================================================================

--------------------------------------------------------------------------------------------------
Create a ReactJS Project
--------------------------------------------------------------------------------------------------
    
    - Create a ReactJS Project ::
        
        yarn create vite tut02-writing-markup-with-jsx --template react-ts
        
    - Move inside the ReactJS project folder <tut02-writing-markup-with-jsx> ::
        
        cd tut02-writing-markup-with-jsx
        
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
          :caption: contents of eslint.config.js
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
          
--------------------------------------------------------------------------------------------------
Create Project Contents
--------------------------------------------------------------------------------------------------
    
    - Create the src/list-styles.css file with the following contents
        
        .. code-block:: css
          :caption: src/list-styles.css
          :linenos:
          
          .list-container {
            max-width: 600px;
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
          
        
    - Edit the src/App.tsx file with the following contents
        
        .. code-block:: cfg
          :caption: src/App.tsx
          :linenos:
          
          import { useState } from "react";
          import "./App.css";
          import "./list-style.css";
          
          function App() {
            const [count, setCount] = useState(0);
            const titleElement = <>The Rules of JSX</>;
            const textContent = "JSX Expressions";
            const classNames = "red-color bg-blue";
            const person = {
              name: "George Bush",
              theme: {
                backgroundColor: "black",
                color: "pink",
              },
            };
            function handleClick() {
              setCount((count) => count + 1);
            }
            return (
              <div className="list-container">
                <h2>{titleElement}</h2>
                <ol>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Return a single root element</h3>
                      <p>&quot;&lt;&gt;The Rules of JSX&lt;/&gt;&quot;</p>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Attributes in JSX</h3>
                      <p>&lt;p className=&quot;red-color&quot;&gt;Red&lt;/p&gt;</p>
                      <p className="red-color">Red</p>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Event Handling</h3>
                      <p>
                        &lt;button onClick=&#123;handleClick&#125;&gt;count is
                        &#123;count&#125;&lt;/button&gt;
                      </p>
                      <p>
                        <button onClick={handleClick}>count is {count}</button>
                      </p>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>JavaScript Expressions: Attributes</h3>
                      <p>const classNames=&quot;red-color bg-blue&quot;</p>
                      <p>&lt;p className=&#123; classNames &#125;&gt;Red&lt;/p&gt;</p>
                      <p className={classNames}>Red</p>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>JavaScript Expressions: Contents</h3>
                      <p>const textContent= &quot;JSX Expressions&quot;;</p>
                      <p>
                        &lt;p
                        className=&quot;blue-color&quot;&gt;&#123;textContent&#125;&lt;
                        /p&gt;
                      </p>
                      <p className="blue-color">{textContent}</p>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>Inline CSS Styles</h3>
                      <p>
                        &lt;p style=&#123;&#123; backgroundColor: &quot;grey&quot;, color:
                        &quot;blue&quot;
                        <br /> &#125;&#125; &gt; Grey background with blue text &lt;
                        /p&gt;
                      </p>
                      <p style={{ backgroundColor: "grey", color: "blue" }}>
                        Grey background with blue text
                      </p>
                    </div>
                  </li>
                  <li className="list-item">
                    <div className="list-item-number"></div>
                    <div className="list-item-content">
                      <h3>JavaScript Objects</h3>
                      <div style={{ textAlign: "left" }}>
                        const person = &#123;
                        <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;name: &quot;George Bush&quot;,
                        <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;theme: &#123;
                        <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;backgroundColor: &quot;black&quot;,
                        <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;color: &quot;pink&quot;, &#125;
                        <br />
                        &#125;;
                      </div>
                      <p>
                        &lt;p style=&#123;person.theme&#125;&gt;&#123;person.name&#125;
                        &lt;/p&gt;
                      </p>
                      <p style={person.theme}>{person.name}</p>
                    </div>
                  </li>
                </ol>
              </div>
            );
          }
          
          export default App;
          
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
        - set base to ``/react-projects/react-projects-with-typescript/tut02-writing-markup-with-jsx/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut02-writing-markup-with-jsx/",
            })
            
    - Build the app ::
        
        yarn run build
        
--------------------------------------------------------------------------------------------------
Hosting the App 
--------------------------------------------------------------------------------------------------
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut02-writing-markup-with-jsx/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut02-writing-markup-with-jsx/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``/react-projects-with-typescript/tut02-writing-markup-with-jsx/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut02-writing-markup-with-jsx
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut02-writing-markup-with-jsx/
    - Screenshot
        
        .. figure:: images/tut02/tut02-writing-jsx-homepage.png
           :align: center
           :class: sd-my-2
           :width: 100%
           :alt: Writing Markup with JSX
           
           :custom-color-primary-bold:`Writing Markup with JSX`