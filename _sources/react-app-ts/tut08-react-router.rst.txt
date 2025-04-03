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
    
React Router is a standard library for routing in React applications. It allows you to define navigation within your React app, enabling the rendering of different components based on the URL path. React Router allows you to handle dynamic URLs, nested routes, and more advanced routing mechanisms, making it a powerful tool for building single-page applications (SPAs).

An overview of what React Router looks like:
    
    - BrowserRouter: The router that uses the HTML5 history API.
    - Routes: Container for Route components
    - Declarative Routing: Defining routes directly with <Route /> components.
    - element prop: Renders components in the route
    - Nested Routing with Outlet: Enables parent-child route rendering.
    - Programmatic Navigation: Using useNavigate for route manipulation.
    - Link: Used for navigation between routes without page reloads.
    - Outlet: Placeholder for rendering nested routes inside a parent component.
    - useNavigate: Programmatic navigation for routing within components.
    - useLocation: Access the current location (URL) object, useful for querying URL parameters and state.
    
Key Concepts in React Router:
    
    - Router: The top-level component that holds the route information. There are different types of routers:
        
        - BrowserRouter: Uses the HTML5 history API to keep the UI in sync with the URL.
        - HashRouter: Uses URL hash (#) for routing, suitable for environments where the HTML5 history API isn't available.
        - MemoryRouter: Keeps the history in memory (useful for non-browser environments).
        
    - Routes: A component that holds the Route components. It is used to define different paths and map them to specific components.
    - Route: Represents a single route and the associated component that should be rendered when the route is matched.
    - Link: Allows users to navigate to different routes without a full page reload (client-side navigation).
    - Outlet: A placeholder for rendering nested routes in React Router v6 and beyond.
    - useNavigate and useLocation: Hooks provided by React Router for programmatic navigation and getting information about the current location (URL).
    
    
==================================================================================================
Top Level Routing
==================================================================================================

- Top Level Routing Components:
    
    - Home
    - NotFound
    
- Define Routes: ::
    
    {/* Define Routes */}
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/not-found" element={<NotFound />} />
      ....
    </Routes>
    
- Define Navigation Links: ::
    
    {/* Navigation Links */}
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/not-found">Not Found</Link></li>
        ....
      </ul>
    </nav>
    
- Routing components:
    
    - Define the <Home /> component
        
        .. code-block:: tsx
          :caption: src/Home.tsx
          :linenos:
          
          import "./../App.css";
          
          const Home = () => {
            return <h2 className="App">Home Page</h2>;
          };
          
          export default Home;
          
    - Define the <NotFound /> component
        
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
In React, nested routing refers to having routes inside other routes. This is useful when you want to create a hierarchical structure where one route can display child components as part of its rendering.

- Navlink:  ::
    
    # Top
    {/* Navigation Links */}
    <nav>
      <ul>
        ...
        <li><Link to="/dashboard">Dashboard</Link></li>
      </ul>
    </nav>
    # nested (optional)
    <nav>
      <ul>
        <li><Link to="/dashboard/settings">Settings</Link></li>
        <li><Link to="/dashboard/profile">Profile</Link></li>
      </ul>
    </nav>
    
    

- Route: ::
    
    {/* Dashboard with nested routes */}
    <Route path="/dashboard" element={<Dashboard />}>
      {/* Nested Routes inside Dashboard */}
      <Route path="settings" element={<Settings />} />
      <Route path="profile" element={<Profile />} />
    </Route>
    
- Outlet: for rendering child routes. ::
    
    <div>
      ....
      <nav>
        {/* Navigation Links */}
        <ul>
          <li><Link to="settings">Settings</Link></li>
          <li><Link to="profile">Profile</Link></li>
        </ul>
      </nav>
      {/* This is where the nested routes will be rendered */}
      <Outlet />
    </div>
    
- Routing Components: 
    
    - Nested Routing Components:
        
        - Dashboard
            
            - Profile
            - Settings
            
    - Define the <Dashboard /> component
        
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
          
    - Define the child <Profile /> component
        
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
          
    - Define the child <Settings /> component
        
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
React Router allows you to dynamically render components based on the URL, which is essential for creating dynamic, parameterized routes. Configure dynamic routes by using React Router’s Route component, where the path can include dynamic parameters, such as :productId, which will be captured and passed to the component. A route parameter is a segment in the path that varies. The value of the variable segment is available to components so that they can render something conditionally. In the following path, 1234 is the ``id`` of a customer('/customer/:id'): /customers/1234/

There are two main steps to use dynamic routing:
    
    - First, defined route parameters in a route ::
        
        # Single
        { path: '/customer/:id', element: <Customer /> }
        # Multiple
        { path: '/customer/:customerId/tasks/:taskId', element: <Customer /> }
        
    - Second, use route parameters in components using React Router’s useParams hook. ::
        
        # for route: { path: '/customer/:customerId/tasks/:taskId', element: <Customer /> }
        const params = useParams<Params>()
        console.log('Customer id', params.customerId);
        console.log('Task id', params.taskId);
        

- Dynamic Routing Components structure :
    
    - Dynamic Routing Components:
        
        - Products
            
            - Product 1
            - Product 2
            - Product 3
            
- Dynamic Routing Components:
     
    - Define the <Products /> component
        
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
          
    - Define the child <ProductDetails /> component
        
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
In React, lazy loading is a technique used to defer loading of components until they are needed, which can improve the performance of your app by reducing the initial bundle size. React provides a built-in way to achieve this with the React.lazy function and Suspense component.

There are two main steps to lazy loading React components:
    
    - First, the component must be dynamically imported as follows (Note: the lazy page must be a default export): ::
        
        const LazyPage = lazy(() => import('./LazyPage'));
        
    - The second step is to render the lazy component inside React’s Suspense component as follows: ::
        
        <Route
            path="lazy"
            element={
                <Suspense fallback={<div>Loading…</div>}>
                    <LazyPage />
                </Suspense>
            }
        />
        
    - It's a good idea to use an Error Boundary around components that are lazily loaded, to handle errors in case the component fails to load:
        
        - Class ErrorBoundary ::
            
            class ErrorBoundary extends Component {
              state = { hasError: false };
            
              static getDerivedStateFromError() {
                return { hasError: true };
              }
            
              componentDidCatch(error, info) {
                console.error('Error loading component:', error, info);
              }
            
              render() {
                if (this.state.hasError) {
                  return <div>Something went wrong!</div>;
                }
            
                return this.props.children;
              }
            }
            
        - Lazy loading ::
            
            <Suspense fallback={<div>Loading...</div>}>
                <ErrorBoundary>
                    <MyComponent />
                </ErrorBoundary>
            </Suspense>
            

Lazy loading Components:
    
    - Define the <About /> component.
        
        .. code-block:: tsx
          :caption: src/About.tsx
          :linenos:
          
          import { useState } from "react";
          import "./../App.css";
          
          const About = () => {
            const [count, setCount] = useState(0);
          
            if (count === 3) {
              throw new Error("Intentional error");
            }
          
            return (
              <div>
                <h2 className="App">About Page</h2>
                <h4>{count}</h4>
                <button onClick={() => setCount(count + 1)}>Increment</button>
              </div>
            );
          };
          
          export default About;
    
    - Define the <ErrorBoundary /> component.
        
        .. code-block::
          :caption: src/ErrorBoundary.tsx
          :linenos:
          
          import React, { Component, ReactNode } from "react";
          
          // Define the types for the state and props of the ErrorBoundary component
          interface ErrorBoundaryState {
            hasError: boolean;
            error?: Error | null;
            errorInfo?: React.ErrorInfo | null;
          }
          
          interface ErrorBoundaryProps {
            children: ReactNode;
          }
          
          class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
            constructor(props: ErrorBoundaryProps) {
              super(props);
              this.state = { hasError: false, error: null, errorInfo: null };
            }
          
            // This lifecycle method is called when an error is thrown in a child component
            static getDerivedStateFromError(error: Error): ErrorBoundaryState {
              // Update the state so the next render will show the fallback UI
              return { hasError: true, error };
            }
          
            // This lifecycle method is called after an error is caught
            componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
              // You can log the error to an error reporting service
              console.error("Error caught by ErrorBoundary:", error, errorInfo);
              this.setState({
                error,
                errorInfo,
              });
            }
          
            render() {
              if (this.state.hasError) {
                // Render a fallback UI when an error is caught
                return (
                  <div>
                    <h2>Something went wrong.</h2>
                    <details style={{ whiteSpace: "pre-wrap" }}>
                      {this.state.error && this.state.error.toString()}
                      <br />
                      {this.state.errorInfo && this.state.errorInfo.componentStack}
                    </details>
                  </div>
                );
              }
          
              // If there's no error, render the children normally
              return this.props.children;
            }
          }
          
          export default ErrorBoundary;
          
==================================================================================================
Function Component - the User Interface
==================================================================================================
    
    - Edit ``App.tsx`` to show the user interface and render the components:
        
        .. code-block:: tsx
          :caption: src/App.tsx
          :linenos:
          
          import { BrowserRouter, Route, Routes, NavLink } from "react-router";
          import Home from "./pages/Home";
          import NotFound from "./pages/NotFound";
          import Dashboard from "./pages/Dashboard";
          import Profile from "./pages/Profile";
          import Settings from "./pages/Settings";
          import Products from "./pages/Products";
          import ProductDetails from "./pages/ProductDetails";
          //import About from "./pages/About";
          import ErrorBoundary from "./pages/ErrorBoundary";
          import { lazy, Suspense } from "react";
          
          function App() {
            const isActiveStyle = ({ isActive }: { isActive: boolean }) => ({
              color: isActive ? "red" : "black",
              fontWeight: isActive ? "bold" : "normal",
              textDecoration: "none",
              marginRight: "15px",
            });
            const About = lazy(() => import("./pages/About"));
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
                        Dashboard
                      </NavLink>
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
                  <Route
                    path="/about"
                    element={
                      <Suspense fallback={<div>Loading...</div>}>
                        <ErrorBoundary>
                          <About />
                        </ErrorBoundary>
                      </Suspense>
                    }
                  />
          
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
           
