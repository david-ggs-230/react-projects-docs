.. _tut05-function-components-hooks:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Function Components - Hooks
##################################################################################################

React Hooks are functions that let you **"hook into"** React state and lifecycle features from function components. Hooks were added to React in version 16.8. React hooks are a powerful feature that allow you to use state, lifecycle methods, and other React features in functional components. 

React Hooks are powerful tools, but they come with certain rules to ensure that they work as expected. These rules must be followed to avoid unexpected behavior in your components. Here are the core rules for using React Hooks:
    
    -  Only Call Hooks at the Top Level
        
        Hooks must be called at the top level of your component or custom hook. They cannot be called conditionally or inside loops or nested functions. This ensures that hooks are always called in the same order on every render. Calling hooks conditionally or inside loops could result in them being invoked in a different order on different renders, leading to bugs and unpredictable behavior.
        
    - Only Call Hooks from React Functions
        
        You can only call hooks from React function components or custom hooks. You cannot use hooks in regular JavaScript functions or class components. Hooks rely on the React rendering lifecycle. Using hooks outside of React components means React can’t keep track of them properly.
        
    - Use Hooks in Custom Hooks
        
        If you are building custom hooks, you can call other hooks within them, but they must still follow the same rules: hooks must be called at the top level and only inside function components or other custom hooks. Custom hooks must still follow the rules of hooks. Calling hooks conditionally or in loops will break React’s rules and lead to unpredictable results.
        
    - Hooks Must Be Called in the Same Order
        
        Each hook call must be executed in the same order every time the component renders. This means you cannot call hooks based on conditions, such as inside if statements or loops. React needs to track the order in which hooks are called, so skipping or reordering hooks can break React’s internal state tracking.
        
    - Calling hooks conditionally
        
        If you need conditional logic, you can use hooks, but make sure the hooks themselves are not called conditionally. You can use conditionals inside the hook function.
        
    - Custom Hook names
        
        By convention, custom hook names should start with use (e.g., useCounter, useFetch), which ensures that React can enforce the rules of hooks.
        
        
The main hooks include useState, useEffect, useContext, useReducer, useCallback, useMemo, useRef, and useImperativeHandle, among others. These hooks provide ways to access React features, allowing you to better organize and reuse your code.

    
.. toctree::
    :maxdepth: 2
    
    tut05-function-components-hooks-usestate
    tut05-function-components-hooks-useeffect
    tut05-function-components-hooks-usecontext
    tut05-function-components-hooks-useref
    
