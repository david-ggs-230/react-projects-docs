.. _tut04-class-components:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold


.. rst-class:: title-center h1
   

##################################################################################################
Tut04-React Class Components
##################################################################################################

A React class component is a way to define a component using a JavaScript/TypeScript class. React class components extend from React.Component and typically include methods such as render() to define what the component should display. In React class components, lifecycle methods are used to handle various stages of a component’s lifecycle. These methods are triggered at different times, such as when the component is first mounted (added to the DOM), updated due to changes in state or props, and unmounted (removed from the DOM).
    
    - Class components are ES6 classes that extend React.Component.
    - In React class components, the render() method is mandatory and returns JSX that defines the component's display.
    - In a React class component, ``this`` is used to access the component's props, state, and methods.
    - React class components include features like state management and lifecycle methods.
        
        - State Management: State is managed using the this.state property.
        - Lifecycle Methods: Includes methods like componentDidMount, componentDidUpdate, etc.
        

.. toctree::
    :maxdepth: 2
    
    tut04-class-components-props
    tut04-class-components-state
    tut04-class-components-event
    
    