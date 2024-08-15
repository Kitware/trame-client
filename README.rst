trame-client: core client for trame
===========================================================================

.. image:: https://github.com/Kitware/trame-client/actions/workflows/test_and_release.yml/badge.svg
    :target: https://github.com/Kitware/trame-client/actions/workflows/test_and_release.yml
    :alt: Test and Release

trame-client is the generic single page application that come with `trame <https://kitware.github.io/trame/>`_.
trame-client provides the infrastructure on the client-side (browser) to connect to a trame server, synchronize
its state with the server, make method call, load dynamically components and feed a dynamic template provided by the server.

This package is not supposed to be used by itself but rather should come as a dependency of **trame**.
For any specificity, please refer to `the trame documentation <https://kitware.github.io/trame/>`_.


Installing
-----------------------------------------------------------

trame-client can be installed with `pip <https://pypi.org/project/trame-client/>`_:

.. code-block:: bash

    pip install --upgrade trame-client


Usage
-----------------------------------------------------------

The `Trame Tutorial <https://kitware.github.io/trame/docs/tutorial.html>`_ is the place to go to learn how to use the library and start building your own application.

The `API Reference <https://trame.readthedocs.io/en/latest/index.html>`_ documentation provides API-level documentation.

License
-----------------------------------------------------------

trame-client is made available under the MIT License. For more details, see `LICENSE <https://github.com/Kitware/trame-client/blob/master/LICENSE>`_
This license has been chosen to match the one use by `Vue.js <https://github.com/vuejs/vue/blob/dev/LICENSE>`_ which is instrumental for making that library possible.


Community
-----------------------------------------------------------

`Trame <https://kitware.github.io/trame/>`_ | `Discussions <https://github.com/Kitware/trame/discussions>`_ | `Issues <https://github.com/Kitware/trame/issues>`_ | `RoadMap <https://github.com/Kitware/trame/projects/1>`_ | `Contact Us <https://www.kitware.com/contact-us/>`_

.. image:: https://zenodo.org/badge/410108340.svg
    :target: https://zenodo.org/badge/latestdoi/410108340


Enjoying trame?
-----------------------------------------------------------

Share your experience `with a testimonial <https://github.com/Kitware/trame/issues/18>`_ or `with a brand approval <https://github.com/Kitware/trame/issues/19>`_.


Runtime configuration
-----------------------------------------------------------

Trame client is the JS core of trame and can be tuned by url parameters. The table below list which parameters we process and how they affect the client.

.. list-table:: URL parameters
   :widths: 25 75
   :header-rows: 0

   * - enableSharedArrayBufferServiceWorker
     - When set this will load an extra script that will use a service worker to enable SharedArrayBuffer
   * - ui
     - Layout name selector. When a trame app define several layout with different name, you can choose which layout should be displayed
   * - remove
     - By default the URL will be cleaned from trame config parameters (sessionURL, sessionManagerURL, secret, application) but if additional parameters should be removed as well but used in the launcher config, this can be achieved by adding a `&remove=param1,param2`.

The table below leverage environment variables, mainly for the Jupyter Lab context and the iframe builder configuration.

.. list-table:: Environment variables
   :widths: 25 75
   :header-rows: 0

   * - TRAME_JUPYTER_ENDPOINT
     - Used by the trame-jupyter-extension
   * - TRAME_JUPYTER_WWW
     - Used by the trame-jupyter-extension
   * - JUPYTERHUB_SERVICE_PREFIX
     - Used to figure out server proxy path for iframe builder
   * - HOSTNAME
     - When "jupyter-hub-host" is used as iframe builder, the hostname will be lookup using that environment variable
   * - TRAME_IFRAME_BUILDER
     - Specify which iframe builder should be used. If not provided we try to do some smart detection
   * - TRAME_IPYWIDGETS_DISABLE
     - Skip any iPyWidget iframe wrapping

Development
-----------------------------------------------------------

Build client side code base

.. code-block:: console

    cd vue[2,3]-app
    npm install
    npm run build            # build trame client application
    cd -
