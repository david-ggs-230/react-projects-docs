.. _tut01-create-reactjs-app:

.. rst-class:: title-center h1
   

##################################################################################################
Tut01-Create a React App on Windows
##################################################################################################

**************************************************************************************************
Create a React App with Vite
**************************************************************************************************

==================================================================================================
Prerequisites
==================================================================================================
    
    Vite requires Node.js version ≥ 18. and npm version 8. However, some templates require a higher Node.js version to work.
        
        - Node version ≥ 18.
        - NPM version 8.
        
==================================================================================================
Create a ReactJS Project with Vite
==================================================================================================
    
    - Create a folder for the ReactJS projects:
        
        - Create Directory for React Projects ::
            
            mkdir <react-projects-folder>
            
        - Move inside the folder::
            
            cd  <react-projects-folder>
        
    - Create ReactJS App with Vite ::
        
        # npm
        npm create vite@latest <new-react-app-name> -- --template react-ts
        # yarn
        yarn create vite <new-react-app-name> --template react-ts
        
==================================================================================================
Build and Run
==================================================================================================
  
  .. code-block:: sh
    :linenos:
    
    # Move inside the <new-react-app-name> folder
    cd  <new-react-app-name>
    # Run dev:  npm run dev <or> yarn dev
    npm run dev
    # Build the React App: npm run build <or> yarn build
    npm run build
    # preview:  npm run preview <or> yarn preview
    npm run preview
    
==================================================================================================
Hosting the React App on GitHub Pages
==================================================================================================

    
    - Creating a github repo, ``main`` branch
    - Create a ``gh-pages`` branch
    - Enable GitHub Pages by configuring ``Settings`` -> ``Pages``
    - Create the deploying base folder in the ``gh-pages`` branch
        
        - if deploying to `https://<USERNAME>.github.io/<repo-name>/<deploying-base-dir>/<sub-dir>/ <https://\<USERNAME\>.github.io/\<repo-name\>/\<deploying-base-dir\>/\<sub-dir\>/>`_, then create:
            
            - in the ``gh-pages`` branch, create ``/<repo-name>/<deploying-base-dir>/<sub-dir>/`` folder structure
            - upload the build files to `https://github.com/<USERNAME>/<repo-name>/<deploying-base-dir>/<sub-dir>/ <https://github.com/\<USERNAME\>/\<repo-name\>/\<deploying-base-dir\>/\<sub-dir\>/>`_ in the ``gh-pages`` branch
            - the deploying base is ``/<repo-name>/<deploying-base-dir>/<sub-dir>/``
            - the deploying url: ``https://<USERNAME>.github.io/<repo-name>/<deploying-base-dir>/<sub-dir>/``
            
        - Configure the build base url:
            
            - open vite.config.js file
            - set base to ``/<repo-name>/<deploying-base-dir>/<sub-dir>/`` ::
                
                export default defineConfig({
                    plugins: [react()],
                    base: '/<repo-name>/<deploying-base-dir>/<sub-dir>/',
                })
                
    - Build the app ::
        
        # npm
        npm run build
        # yarn
        yarn run build
        
    - Push the <dist> folder contents to the deploying base folder in the ``gh-pages`` branch
    

**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut01-create-reactjs-app
    - Demo site: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut01-create-reactjs-app/
    