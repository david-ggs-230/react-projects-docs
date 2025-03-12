.. _tut05-function-components:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Tut05-React Function Components
##################################################################################################

React Function Components are a way to define components in React using JavaScript functions. They are simpler and more concise than class components, making them popular for modern React development. In function components, you can use hooks like useState, useEffect, and other React hooks to manage state and lifecycle events. Functional components can accept props as input and return JSX that describes what the component should render.
    
    - Stateless (before hooks): Originally, functional components were stateless and used only for rendering UI based on props.
    - Simpler Syntax: They are defined as JavaScript functions, leading to cleaner and more readable code.
    - Return JSX: Functional components return JSX (a syntax extension that allows HTML-like code inside JavaScript).
    - No, this keyword: Unlike class components, functional components do not have a this context.
    - Hooks: With hooks, functional components can manage state and side effects, making them just as powerful as class components.
    

When a functional component receives input and is rendered, React uses props and updates the virtual DOM to ensure the UI reflects the current state:
    
    - Props: Functional components receive input data through props, which are objects containing key-value pairs.
    - Processing Props: After receiving props, the component processes them and returns a JSX element that defines the component’s structure and content.
    - Virtual DOM: When the component is rendered, React creates a virtual DOM tree that represents the current state of the application.
    - Re-rendering: If the component’s props or state change, React updates the virtual DOM tree accordingly and triggers the component to re-render.
    
Functional components should be used whenever possible because they are simpler, easier to test, and more performant than class components. ReactJS functional components offer several benefits over class components, including:
    
    - Simplicity: Functional components are simpler and easier to read than class components, making them ideal for small to medium-sized projects.
    - Performance: Functional components are faster than class components because they don’t use the this keyword, which can slow down rendering.
    - Testability: Functional components are easier to test because they are stateless and don’t rely on lifecycle methods.
    - Reusability: Functional components can be reused across multiple projects, making them a great choice for building component libraries.
    
    
.. toctree::
    :maxdepth: 2
    
    tut05-function-components-props
    tut05-function-components-state
    tut05-function-components-event
    tut05-function-components-life-cycle
    
    