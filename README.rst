trame-html: core client for trame
===========================================================================

trame-client is the generic single page application that come with `trame <https://kitware.github.io/trame/>`_.
trame-client provides the infrastructure on the client-side (browser) to connect to a trame server, synchronize
its state with the server, make method call, load dynamically components and feed a dynamic template provided by the server.

This package is not supposed to be used by iteself but rather should come as a dependency of **trame**.
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

This library specifically brings the following set of vue.js components to the core client side application.
They will be available as a library on NPM to support trame integration into existing vue.js based application.

.. code-block:: html

    <trame-connect name="TrameConnect" :config="{}" :exclude="[]" use-url forward-errors>
        <trame-server-template template-name="main" />

        <trame-loading message="welcome" />

        <trame-state-resolver :names="['a', 'b', 'c']" v-slot="{a, b, c, set, trame}">
            <div>
                <div>
                    A: {{ a }}
                </div>
                <div>
                    B: {{ b }}
                </div>
                <div>
                    C: {{ c }}
                </div>
                <br>
                <button @click="trame.state.set('a', a + 1)">A+</button>
                <br>
                <button @click="set('a', a - 1)">A-</button>
                <br>
                <button>B</button>
                <br>
                <button>C</button>
            </div>
        </trame-state-resolver>
    </trame-connect>

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


Development
-----------------------------------------------------------

Build client side code base

.. code-block:: console

    cd vue-app
    npm i
    npm run build            # build trame client application
    npm run build:components # build trame components for integration purpose
    cd -
