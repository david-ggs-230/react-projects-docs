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
    
    - Create a ReactJS Project ::
        
        yarn create vite tut02-writing-markup-with-jsx --template react-ts
        
    - Move inside the ReactJS project folder <tut02-writing-markup-with-jsx> ::
        
        cd tut02-writing-markup-with-jsx
        
    - Create the src/list-styles.css file with the following contents
        
        .. code-block:: sh
          :caption: src/list-styles.css
          :linenos:
          
          .listcontainer {
            font-family: "Space Mono", monospace;
            display: flex;
            flex-direction: column;
            max-width: 800px;
            padding: 32px;
            margin: 60px auto;
            border: 1px solid #eee;
            box-shadow: 0px 12px 24px rgba(0, 0, 0, 0.06);
          }
          
          * {
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            text-rendering: optimizelegibility;
            letter-spacing: -0.25px;
          }
          
          ol {
            padding-left: 50px;
          }
          
          li {
            color: #4f4f4f;
            padding-left: 16px;
            margin-top: 24px;
            position: relative;
            font-size: 16px;
            line-height: 20px;
          }
          
          li:before {
            content: "";
            display: block;
            height: 42px;
            width: 42px;
            border-radius: 50%;
            border: 2px solid #ddd;
            position: absolute;
            top: -12px;
            left: -46px;
          }
          
          ol.alternating-colors li:nth-child(odd):before {
            border-color: #0bad02;
          }
          
          ol.alternating-colors li:nth-child(even):before {
            border-color: #2378d5;
          }
          
          .red-color{
            color: #ff0000;
          }
          
          .blue-color{
            color: #0011ff;
          }
          
          .bg-red{
            background-color: #ff0000;
          }
          
          .bg-blue{
            background-color: #0011ff;
          }
          
        
        
    - Edit the src/App.tsx file with the following contents
        
        .. code-block:: sh
          :caption: src/App.tsx
          :linenos:
          
          import { useState } from "react";
          import "./App.css";
          import "./list-style.css";
          
          function App() {
            const [count, setCount] = useState(0);
            const titleElement = <>The Rules of JSX</>;
            const textContent= "JSX Expressions";
            const classNames = "red-color bg-blue";
            const person = {
              name: 'George Bush',
              theme: {
                backgroundColor: 'black',
                color: 'pink'
              }
            };
            function handleClick() {
              setCount((count) => count + 1);
            }
            return (
              <div className="App listcontainer">
                <h2>{titleElement}</h2>
                <ol className="alternating-colors">
                  <li>
                    <strong>Return a single root element</strong>
                    <div>&quot;&lt;&gt;The Rules of JSX&lt;/&gt;&quot;</div>
                  </li>
                  <li>
                    <strong>Attributes in JSX</strong>
                    <div>
                      <div>&lt;div className="red-color"&gt;Red&lt;/div&gt;</div>
                      <div className="red-color">Red</div>
                    </div>
                  </li>
                  <li>
                    <strong>Event Handling</strong>
                    <div>
                      <button onClick={handleClick}>count is {count}</button>
                    </div>
                  </li>
                  <li>
                    <strong>JavaScript Expressions</strong>
                    <div>
                      <div>const classNames="red-color bg-blue"</div>
                      <div>
                        &lt;div className=&#123; classNames &#125;&gt;Red&lt;/div&gt;
                      </div>
                      <div className={classNames}>Red</div>
                      <div>const textContent= "JSX Expressions";</div>
                      <div>
                        &lt;div className="blue-color"&gt;&#123;textContent&#125;&lt;/div&gt;
                      </div>
                      <div className="blue-color">{textContent}</div>
                    </div>
                  </li>
                  <li>
                    <strong>JavaScript Objects and CSS</strong>
                    <div>
                      <div> &lt;div style=&#123;&#123;backgroundColor:'grey',color:'blue'&#125;&#125;&gt;...&lt;/div&gt;</div>
                      <div style={{ backgroundColor: 'grey', color: 'blue' }}>Grey with blue text</div>
                      <div>
                        &lt;div style=&#123;person.theme&#125;&gt;&#123;person.name&#125; &lt;/div&gt;
                      </div>
                      <div style={person.theme}>{person.name}</div>
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
    
    If deploying to `https://<USERNAME>.github.io/<repo-name>/<deploying-base-dir>/<sub-dir>/ <https://\<USERNAME\>.github.io/\<repo-name\>/\<deploying-base-dir\>/\<sub-dir\>/>`_, then create:
            
            - in the ``gh-pages`` branch, create ``/<repo-name>/<deploying-base-dir>/<sub-dir>/`` folder structure
            - upload the build files to `https://github.com/<USERNAME>/<repo-name>/<deploying-base-dir>/<sub-dir>/ <https://github.com/\<USERNAME\>/\<repo-name\>/\<deploying-base-dir\>/\<sub-dir\>/>`_ in the ``gh-pages`` branch
            - the deploying base is ``/<repo-name>/<deploying-base-dir>/<sub-dir>/``
            - the deploying url: ``https://<USERNAME>.github.io/<repo-name>/<deploying-base-dir>/<sub-dir>/``
    
    - Configure the build base url:
        
        - open vite.config.js file
        - set base to ``/react-projects/react-projects-with-typescript/tut02-writing-markup-with-jsx/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: '/react-projects/react-projects-with-typescript/tut02-writing-markup-with-jsx/',
            })
            
    - Build the app ::
        
        yarn run build
        
    - Push the <dist> folder contents to the deploying base folder in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut02-writing-markup-with-jsx
    - Demo site: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut02-writing-markup-with-jsx/
    - Screenshot
        
        .. figure:: images/tut02/tut02-writing-jsx-homepage.png
           :align: center
           :class: sd-my-2
           :width: 50%
           :alt: Writing Markup with JSX
           
           :custom-color-primary-bold:`Writing Markup with JSX`