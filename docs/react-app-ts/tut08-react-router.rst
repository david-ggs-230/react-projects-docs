.. _tut08-react-router:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
React Router
##################################################################################################

A router is responsible for selecting what to show in the app for a requested path. React Router is a routing library for React apps. React Router provides several components to help manage navigation and routing in a React application. The primary components for handling routing and navigation are:
    
    - Installing React Router ::
        
        # npm
        npm i react-router
        # yarn
        yarn add react-router
        
    - BrowserRouter (or Router for custom history) - Router is th top level component. It encloses the entire application.
    - Route − The Route component is used to define which components to render based on the current URL path ::
        
        <Route path="/home" element={<Home />} />
        
    - Link - The Link component is used to create navigational links in the app that change the URL when clicked, without causing a full page reload. It's a replacement for the traditional <a> tag for navigation in a React SPA. ::
        
        # Here, to attribute is used to set the target url.
        <Link to="/">Home</Link>
        
    - Routers - Routers is used to group Route components, rendering the first Route or Redirect that matches the current location.  ::
        
        <Routers>
          <Route path="/home" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/not-found" element={<NotFound />} /> 
          {/* Fallback route for 404 */}
          <Route path="*" element={<NotFound />} /> 
        </Routers>
        
    - Redirect - Redirects the user to a different route when a certain condition is met (e.g., after a login).
    - useHistory, useLocation, useParams, useRouteMatch - These hooks allow you to access the history, location, route parameters, and match data in functional components.
    
    
**************************************************************************************************
Create a React Project Structure
**************************************************************************************************

==================================================================================================
Create a React Project
==================================================================================================
    
    - Create a ReactJS Project ::
        
        yarn create vite tut08-react-router --template react-ts
        
    - Move inside the ReactJS project folder <tut08-react-router> ::
        
        cd tut08-react-router
        
    - Install the dependencies ::
        
        yarn install
        
    - Install the react-router library dependencies ::
        
        yarn add react-router
        
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
React Router Components
**************************************************************************************************

Routing Components structure :
    
    - Home
    - About
    - Dashboard
        
        - Profile
        - Settings
        
    - Products
        
        - Product 1
        - Product 2
        - Product 3
        
    - NotFound
    
==================================================================================================
Top Level Routing
==================================================================================================
    
    - Top Level Routing Components:
        
        - Home
        - About
        - NotFound
        
    - Define the <Home /> component ::
        
        .. code-block:: tsx
          :caption: src/Home.tsx
          :linenos:
          
          import "./../App.css";
          
          const Home = () => {
            return <h2 className="App">Home Page</h2>;
          };
          
          export default Home;
          
    - Define the <About /> component ::
        
        .. code-block:: tsx
          :caption: src/About.tsx
          :linenos:
          
          import "./../App.css";
          
          const About = () => {
            return <h2 className="App">About Page</h2>;
          };
          
          export default About;
          
    - Define the <NotFound /> component ::
        
        .. code-block:: tsx
          :caption: src/NotFound.tsx
          :linenos:
          
          import "./../App.css";
          
          const NotFound = () => {
            return <h2 className="App">Page Not Found</h2>;
          };
          
          export default NotFound;
          
==================================================================================================
Nested Routing
==================================================================================================
    
    - Nested Routing Components:
        
        - Dashboard
            
            - Profile
            - Settings
            
    - Define the <Dashboard /> component ::
        
        .. code-block:: tsx
          :caption: src/Dashboard.tsx
          :linenos:
          
          import { Link, Outlet } from "react-router";
          import "./../App.css";
          
          const Dashboard = () => {
            return (
              <div
                className="App"
                style={{
                  borderWidth: "1px",
                  borderStyle: "solid",
                  borderColor: "red",
                  padding: "10px",
                }}
              >
                <h2>Parent Component</h2>
                <h4>Dashboard with Nested Routing</h4>
                <nav
                  style={{
                    borderWidth: "1px",
                    borderStyle: "solid",
                    borderColor: "blue",
                  }}
                >
                  <div>Link inside the parent component</div>
                  <ul
                    style={{
                      listStyle: "none",
                    }}
                  >
                    <li>
                      <Link to="profile">Profile</Link>
                    </li>
                    <li>
                      <Link to="settings">Settings</Link>
                    </li>
                  </ul>
                </nav>
                <Outlet />
              </div>
            );
          };
          
          export default Dashboard;
          
    - Define the child <Profile /> component ::
        
        .. code-block:: tsx
          :caption: src/Profile.tsx
          :linenos:
          
          import "./../App.css";
          
          const Profile = () => {
            return (
              <div
                style={{
                  borderWidth: "1px",
                  borderStyle: "solid",
                  borderColor: "green",
                  marginTop: "20px",
                }}
              >
                <h2 className="App">Nested Child Components</h2>
                <h4 className="App">Profile Contents</h4>
              </div>
            );
          };
          
          export default Profile;
          
    - Define the child <Settings /> component ::
        
        .. code-block:: tsx
          :caption: src/Settings.tsx
          :linenos:
          
          import "./../App.css";
          
          const Settings = () => {
            return (
              <div
                style={{
                  borderWidth: "1px",
                  borderStyle: "solid",
                  borderColor: "green",
                  marginTop: "20px",
                }}
              >
                <h2 className="App">Nested Child Components</h2>
                <h4 className="App">Settings Contents</h4>
              </div>
            );
          };
          
          export default Settings;
          
==================================================================================================
Dynamic Routing
==================================================================================================
    
    - Dynamic Routing Components:
        
        - Products
            
            - Product 1
            - Product 2
            - Product 3
            
    - Define the <Products /> component ::
        
        .. code-block:: tsx
          :caption: src/Products.tsx
          :linenos:
          
          import { Link, Outlet } from "react-router";
          import "./../App.css";
          
          const Products = () => {
            return (
              <div
                className="App"
                style={{
                  borderWidth: "1px",
                  borderStyle: "solid",
                  borderColor: "red",
                  padding: "10px",
                }}
              >
                <h2>Parent Component</h2>
                <h4>Products with Nested Routing</h4>
                <nav
                  style={{
                    borderWidth: "1px",
                    borderStyle: "solid",
                    borderColor: "blue",
                  }}
                >
                  <div>Link inside the parent component</div>
                  <ul style={{ listStyle: "none" }}>
                    <li>
                      <Link to="/products/1">Product 1</Link>
                    </li>
                    <li>
                      <Link to="/products/2">Product 2</Link>
                    </li>
                    <li>
                      <Link to="/products/3">Product 3</Link>
                    </li>
                  </ul>
                </nav>
                <Outlet />
              </div>
            );
          };
          
          export default Products;
          
    - Define the child <ProductDetails /> component ::
        
        .. code-block:: tsx
          :caption: src/ProductDetails.tsx
          :linenos:
          
          import { useParams } from "react-router";
          import "./../App.css";
          
          function ProductDetails() {
            const { productId } = useParams();
            return (
              <div
                style={{
                  borderWidth: "1px",
                  borderStyle: "solid",
                  borderColor: "green",
                  marginTop: "20px",
                }}
              >
                <h2 className="App">Nested Child Components</h2>
                <h4 className="App">Product Contents</h4>
                <h5 className="App">
                  Product ID:
                  <span
                    style={{ color: "blue", fontSize: "1.5rem" }}
                  >{` ${productId}`}</span>
                </h5>
              </div>
            );
          }
          
          export default ProductDetails;
          
==================================================================================================
Lazy Routing
==================================================================================================
    
    - Lazy Routing Components:
        
        - About
            
            - Product 1
            - Product 2
            - Product 3
            
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    - Edit ``App.tsx`` to show the user interface and render the components:
        
        .. code-block:: tsx
          :caption: src/App.tsx
          :linenos:
          
          import { BrowserRouter, Route, Routes, NavLink } from "react-router";
          import Home from "./pages/Home";
          import About from "./pages/About";
          import NotFound from "./pages/NotFound";
          import Dashboard from "./pages/Dashboard";
          import Profile from "./pages/Profile";
          import Settings from "./pages/Settings";
          import Products from "./pages/Products";
          
          import ProductDetails from "./pages/ProductDetails";
          
          function App() {
            const isActiveStyle = ({ isActive }: { isActive: boolean }) => ({
              color: isActive ? "red" : "black",
              fontWeight: isActive ? "bold" : "normal",
              textDecoration: "none",
              marginRight: "15px",
            });
            return (
              <BrowserRouter basename="/react-projects/react-projects-with-typescript/tut08-react-router">
                <nav>
                  <div style={{ display: "flex", gap: "20px" }}>
                    <div>
                      <NavLink style={isActiveStyle} to="/">
                        Home
                      </NavLink>
                    </div>
                    <div>
                      <NavLink style={isActiveStyle} to="/about">
                        About
                      </NavLink>
                    </div>
                    <div>
                      <NavLink style={isActiveStyle} to="/dashboard">
                        <div>Dashboard</div>
          
                        <nav>
                          <ul
                            style={{
                              listStyle: "none",
                              marginTop: "4px",
                            }}
                          >
                            <li>
                              <NavLink style={isActiveStyle} to="/dashboard/profile">
                                Profile
                              </NavLink>
                            </li>
                            <li>
                              <NavLink style={isActiveStyle} to="/dashboard/settings">
                                Settings
                              </NavLink>
                            </li>
                          </ul>
                        </nav>
                      </NavLink>
                    </div>
                    <div>
                      <NavLink style={isActiveStyle} to="/products">
                        Products
                      </NavLink>
                    </div>
                    <div>
                      <NavLink style={isActiveStyle} to="/abcde">
                        Not Found
                      </NavLink>
                    </div>
                  </div>
                </nav>
                <Routes>
                  {/* Define routes */}
                  <Route path="/" element={<Home />} />
                  <Route path="/home" element={<Home />} />
                  <Route path="/about" element={<About />} />
                  <Route path="/dashboard" element={<Dashboard />}>
                    {/* Nested Routes */}
                    <Route path="profile" element={<Profile />} />
                    <Route path="settings" element={<Settings />} />
                  </Route>
          
                  <Route path="/products" element={<Products />}>
                    {/* Dynamic route */}
                    <Route path="/products/:productId" element={<ProductDetails />} />
                  </Route>
                  <Route path="/non-existent" element={<NotFound />} />
                  {/* Fallback route for 404 */}
                  <Route path="*" element={<NotFound />} />
                </Routes>
              </BrowserRouter>
            );
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
        - set base to ``/react-projects/react-projects-with-typescript/tut08-react-router/`` ::
            
            export default defineConfig({
                plugins: [react()],
                base: "/react-projects/react-projects-with-typescript/tut08-react-router/",
            })
            
    - Build the app ::
        
        yarn run build
        
==================================================================================================
Hosting the App 
==================================================================================================
    
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut08-react-router/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut08-react-router/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``react-projects-with-typescript/tut08-react-router/`` in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut08-react-router
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut08-react-router/
    - Screenshot
        
        .. figure:: images/tut08/tut08-react-router.png
           :align: center
           :class: sd-my-2
           :width: 60%
           :alt: React Routers
           
           :custom-color-primary-bold:`React Routers`
           
