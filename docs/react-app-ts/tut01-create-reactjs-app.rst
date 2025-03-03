.. _tut01-create-reactjs-app:

.. role:: custom-color-primary
   :class: sd-text-primary
   
.. role:: custom-color-primary-bold
   :class: sd-text-primary sd-font-weight-bold
   
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
        
        - Create a folder for React Projects ::
            
            mkdir <react-projects-folder>
            
        - Move inside the folder ::
            
            cd  <react-projects-folder>
            
    - Create ReactJS App with Vite ::
        
        # npm: create vite@latest <new-react-app-name> -- --template react-ts
        create vite@latest tut01-create-reactjs-app -- --template react-ts
        # yarn create vite <new-react-app-name> --template react-ts
        yarn create vite tut01-create-reactjs-app --template react-ts
        
==================================================================================================
ESLint and Prettier configuration (Optional)
==================================================================================================
    
    - Install the ``EditorConfig`` extension for VS Code if you haven't already.
    - Add .editorconfig (https://editorconfig.org) to the root of the project ::
        
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
        
        .. code-block:: cfg
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
            "lint": "eslint src --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
            "lint:fix": "eslint src --ext ts,tsx --fix",
          },
          
    - Run ESLint:
        
        .. code-block:: sh
          :linenos:
          
          #npm
          npm run lint
          npm run lint:fix
          #yarn
          yarn lint
          yarn lint:fix
          
==================================================================================================
Build and Run
==================================================================================================
  
  .. code-block:: sh
    :linenos:
    
    # Move inside the <new-react-app-name> folder
    cd tut01-create-reactjs-app
    # Install the dependencies:  npm install <or> yarn install
    npm install
    # Run dev:  npm run dev <or> yarn dev
    npm run dev
    # Build the React App: npm run build <or> yarn build
    npm run build
    # preview:  npm run preview <or> yarn preview
    npm run preview
    
==================================================================================================
Hosting the React App on GitHub Pages
==================================================================================================

--------------------------------------------------------------------------------------------------
Hosting Guide
--------------------------------------------------------------------------------------------------
    
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
                
--------------------------------------------------------------------------------------------------
Host the Live Demo on GitHub Pages
--------------------------------------------------------------------------------------------------

    - Modifiy the ``vite.config.js`` file as follows ::
        
        export default defineConfig({
            plugins: [react()],
            base: '/react-projects/react-projects-with-typescript/tut01-create-reactjs-app/',
        })
        
    - Build the app ::
        
        # npm
        npm run build
        # yarn
        yarn run build
        
    - Hosting address: `https://<USERNAME>.github.io/react-projects/react-projects-with-typescript/tut01-create-reactjs-app/ <https://\<USERNAME\>.github.io/react-projects/react-projects-with-typescript/tut01-create-reactjs-app/>`_
    - Github login as <USERNAME>
    - Create the ``react-projects`` repo if not exist
    - Create the ``gh-pages`` branch in the ``react-projects`` repo if not exist
    - Push the <dist> folder contents to the deploying folder ``/react-projects-with-typescript/tut01-create-reactjs-app/`` in the ``gh-pages`` branch
    
**************************************************************************************************
Sources and Demos
**************************************************************************************************
    
    - Sources: https://github.com/david-ggs-230/react-projects/tree/main/react-projects-with-typescript/tut01-create-reactjs-app
    - Live Demo: https://david-ggs-230.github.io/react-projects/react-projects-with-typescript/tut01-create-reactjs-app/
    - Screenshot
        
        .. figure:: images/tut01/tut01-create-react-app-vite-homepage.png
           :align: center
           :class: sd-my-2
           :width: 50%
           :alt: Create a React App with Vite
           
           :custom-color-primary-bold:`Create a React App with Vite`
    
    