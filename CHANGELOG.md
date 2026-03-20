# CHANGELOG


## v1.0.0 (2026-03-20)

### Bug Fixes

- Add default slot to components
  ([`fbcdeea`](https://github.com/snacksbro/trame-client/commit/fbcdeea32a2c02c329e3e637512757d884d92928))

- Change selenium requirement to playwright
  ([`1870469`](https://github.com/snacksbro/trame-client/commit/1870469f0c3c81d6abbf47f1ec610cce1aa43916))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- Trigger release
  ([`e2a620c`](https://github.com/snacksbro/trame-client/commit/e2a620c6e6b96068e103996961f42b37b3dd5bcf))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- Uniform __init__.py for package
  ([`589e617`](https://github.com/snacksbro/trame-client/commit/589e61793d9903095673f353ddb9aeaa9fd6e0a2))

- **api**: Add doc to method definition
  ([`7bdb00a`](https://github.com/snacksbro/trame-client/commit/7bdb00a58448155225e0f15cdf8523dae578c307))

- **base**: Use <base> for relative url resolution
  ([`1e42189`](https://github.com/snacksbro/trame-client/commit/1e4218967fa4bc6806233df9704ba074261782b8))

- **cache**: Try to prevent web caching
  ([`2bb25a0`](https://github.com/snacksbro/trame-client/commit/2bb25a0a6e8a1e42b3bfe7c652a0c59b375e540d))

- **cfe**: Add chrome 66 compatibility for cfe runtime
  ([`5dc7b5b`](https://github.com/snacksbro/trame-client/commit/5dc7b5b6d7b0f58a461ca1dd2d3522d6d2d686e9))

- **child-server**: Add support for child server in SizeObserver/Style/Script
  ([`ff498fd`](https://github.com/snacksbro/trame-client/commit/ff498fde7ae8537082ca548312a470c2be84671a))

- **CI**: Add initial CI with semantic-release
  ([`51323fd`](https://github.com/snacksbro/trame-client/commit/51323fdcbd9e519dfa594948557cbaf6b30c88ac))

This also fixes any pre-commit issues.

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **ci**: Use pyproject and ruff
  ([`279a0c8`](https://github.com/snacksbro/trame-client/commit/279a0c814ac072b046ae6ae894e863b352eff204))

- **client**: Latest client build
  ([`cfef0b4`](https://github.com/snacksbro/trame-client/commit/cfef0b4c58a462e2f378bf27a89468b20c3679d6))

- **ClientTriggers**: Add built-in exit event
  ([`0103d30`](https://github.com/snacksbro/trame-client/commit/0103d30bc56b2c341935d000f8e9b98cb552971b))

- **debug**: Add helper for finding invalid args
  ([`d1d5c8f`](https://github.com/snacksbro/trame-client/commit/d1d5c8f103ab359db2e002c4c68f7865cfcbc80e))

- **decorators**: Handle promise rejection in FileReader
  ([`114a75e`](https://github.com/snacksbro/trame-client/commit/114a75e671d7ea80eae1d5c0fc75bb4c6d6820c2))

- **decorators**: Replace blob.arrayBuffer with backward-compatible code
  ([`439b50e`](https://github.com/snacksbro/trame-client/commit/439b50eed98b58e1e8eaf25b7f0dd8042bf9ec3b))

`blob.arrayBuffer()` is not available in IE11, which we need to use for the pywebview desktop apps.

We can instead replace it with this code that is more backward-compatible, and it works with IE11.

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **DeepReactive**: Delete removed key
  ([`00417f4`](https://github.com/snacksbro/trame-client/commit/00417f4a213ce67122ddc9cbe40ccb808b7463f5))

- **default-var**: Allow right default to be a dict to update many vars
  ([`ca7a5dc`](https://github.com/snacksbro/trame-client/commit/ca7a5dc96332aa229e1a97f62b003ad69090c395))

- **desktop**: Add edge 18 support
  ([`2238072`](https://github.com/snacksbro/trame-client/commit/2238072e261a76315d4014dc236a0b1793671f3e))

- **directive**: Add helper to register directives
  ([`e2add71`](https://github.com/snacksbro/trame-client/commit/e2add718de76d12bb486144b644eee02fb1deb50))

- **docs**: Fix typo in CHANGELOG.md
  ([`9f1542a`](https://github.com/snacksbro/trame-client/commit/9f1542a1751fae4114cc56607ad3a2c1ef4dde95))

- **download**: Allow promise as content
  ([`87bc3d7`](https://github.com/snacksbro/trame-client/commit/87bc3d7728b4ddca0a24b9466558583cc7fb224e))

- **event**: Remove scroll, resize, select from default
  ([`804206e`](https://github.com/snacksbro/trame-client/commit/804206e02e23d0f14685e8bac81393b951ff27b6))

- **exit**: Close websocket on exit
  ([`e8524b4`](https://github.com/snacksbro/trame-client/commit/e8524b4b20a10b5664200a22b60dba6b0fa7c3a7))

- **getter**: Enable reactive handling of dynamic name value
  ([`0576edd`](https://github.com/snacksbro/trame-client/commit/0576eddc60b0ff329fbfa6d679de2b25650b2fb0))

- **Getter**: Expose name, update(value), updateNested(path, value)
  ([`257669d`](https://github.com/snacksbro/trame-client/commit/257669df9d7cc23e72860bc5cd3c9d7a82ed7482))

- **global**: Expose state methods on global trame.state
  ([`0238651`](https://github.com/snacksbro/trame-client/commit/02386519e1143255861b0fff1015e0ff41f56098))

- **html**: Add v-slot and v-model modifier
  ([`1863cc0`](https://github.com/snacksbro/trame-client/commit/1863cc0cf5330c7bde9207787701d871cd019ec0))

- **html**: New generated html widgets
  ([`c2e5c84`](https://github.com/snacksbro/trame-client/commit/c2e5c844f8b53f3a9d2386093970469de9eb9d39))

- **input**: Support webkitdirectory
  ([`2c084c8`](https://github.com/snacksbro/trame-client/commit/2c084c8d9580707cacef3fdd1e899ef9e4dd183f))

Add support for webkitdirectory parameter for Input element

- **ipywidget**: Can skip ipywidget even if available
  ([`091410b`](https://github.com/snacksbro/trame-client/commit/091410b47bdc1cde402422deb5a116a798da82c7))

- **js**: Allow script/css loading failure
  ([`e46ccf3`](https://github.com/snacksbro/trame-client/commit/e46ccf308a87b42fe84aa6b9fa41349f8276d9d4))

- **js**: Handle exception when accessing cross-origin parent window
  ([`9f12f69`](https://github.com/snacksbro/trame-client/commit/9f12f69b3ed408f5b939e955b3bb985ceba9ff07))

- **jupyter**: Allow base url to be customized
  ([`547b388`](https://github.com/snacksbro/trame-client/commit/547b388968774b6e791330de112cd320c1019b22))

- **jupyter**: Allow jupyter-hub to be autodetected
  ([`4ec5db2`](https://github.com/snacksbro/trame-client/commit/4ec5db21cc855783decf51fe4835fcb2f20b269e))

- **jupyter**: Better base url handling with extension
  ([`fdc7156`](https://github.com/snacksbro/trame-client/commit/fdc7156f84d4a3bc5dd16c843396c03710a282dd))

- **jupyter**: Iframe builders return a dict instead of a str
  ([`083b046`](https://github.com/snacksbro/trame-client/commit/083b046976365c3e222a83bb298bc1f2b755fb57))

- **jupyter**: Kernel generate www when collocated with server
  ([`c883fae`](https://github.com/snacksbro/trame-client/commit/c883faedd0325fbd604112ba7e2194c0a58d1b87))

- **jupyter-hub**: Fix url generator and add auto detect
  ([`3da386c`](https://github.com/snacksbro/trame-client/commit/3da386c220a80fb1c5c7944efabe25e6806fca9f))

- **kwargs**: Fix handling of vue2 of kwargs
  ([`28c463e`](https://github.com/snacksbro/trame-client/commit/28c463e68f1faf306ed5fa89c0e62e7dcd439549))

- **kwargs**: Fix handling of vue3 of kwargs
  ([`2e8815e`](https://github.com/snacksbro/trame-client/commit/2e8815e3ff8c4e853417128714a1103c585d3da2))

- **layout**: Add template name property in AbstractLayout
  ([#48](https://github.com/snacksbro/trame-client/pull/48),
  [`852a461`](https://github.com/snacksbro/trame-client/commit/852a4615f7821e61f1e4c24ab4fe44579c39cd3f))

Co-authored-by: Justine Antoine <justine.antoine@kitware.com>

- **layout**: Keep track of the original root
  ([`66355b3`](https://github.com/snacksbro/trame-client/commit/66355b30e75f7c28937b4d9a41fd939bd8812024))

- **loading**: Use fetch instead of iframe
  ([`d21b992`](https://github.com/snacksbro/trame-client/commit/d21b992def0cd96f393e891c139684e1a46a8059))

- **model/bind/event**: Fix event and directive processing
  ([`c6f6138`](https://github.com/snacksbro/trame-client/commit/c6f6138875201c23382965cf84d0263bea2a406f))

- **mouse-event**: Add missing enter/leave
  ([`dadd593`](https://github.com/snacksbro/trame-client/commit/dadd593b250bb51b026a84a68ed875cef7b07373))

- **msgpack**: Convert msgpack Uint8Array into blob for backward compatibility
  ([`566c274`](https://github.com/snacksbro/trame-client/commit/566c27452bbe20be76d24061bdd00b7c837b9544))

- **numpy**: Add support for numpy 2.0
  ([`b45403b`](https://github.com/snacksbro/trame-client/commit/b45403bc3b684d0040c8ae1ae1014c88ce25a40b))

- **protocol**: Update wslink for protocol resolution
  ([`12b64ab`](https://github.com/snacksbro/trame-client/commit/12b64ab5972b32a835af08af2f3c3aa1529ebe64))

- **py**: Remove python 3.9 requirement
  ([`17f2029`](https://github.com/snacksbro/trame-client/commit/17f2029132b474730e2f794a5053971c39dc9cff))

- **py**: Removed unused component from Python
  ([`d581e43`](https://github.com/snacksbro/trame-client/commit/d581e432ecffed7a1e325276ac5da3c7bf087e0e))

- **ready**: Remove unused future
  ([`9b1eb0c`](https://github.com/snacksbro/trame-client/commit/9b1eb0cb3d622303ac153a85d5f78cf8777b3c1a))

- **Reconnect**: Allow template name to be used
  ([`3cad023`](https://github.com/snacksbro/trame-client/commit/3cad0237582f46fe0f46e726b5fa1d9b71812f6b))

- **refs**: Start on js_call/ref handling
  ([`3aa2c53`](https://github.com/snacksbro/trame-client/commit/3aa2c531cc4ed20773d5f83cb6ae95a7169f3e47))

- **retry**: Provide empty retry array in html
  ([`9e7ee79`](https://github.com/snacksbro/trame-client/commit/9e7ee79d9e055dbd45f6a995e09b835cdfa6baec))

- **router**: Add infrastructure to handle routes for vue3
  ([`021f871`](https://github.com/snacksbro/trame-client/commit/021f87133240878536e27356dc87feb79ce1784f))

- **script**: Add script tag to client widgets
  ([`1e94bdf`](https://github.com/snacksbro/trame-client/commit/1e94bdf2e5e93c400ec515c1c0397310327af31b))

- **security**: Clean url from trame search params
  ([`f0e093b`](https://github.com/snacksbro/trame-client/commit/f0e093bdaf57a086ca0dfe82d5c67110f9124916))

- **sessionManagerURL**: Add option to read it from the html element dataset
  ([`7d174c4`](https://github.com/snacksbro/trame-client/commit/7d174c4fbbe371eb59023da553305b1d9a6a52c0))

- **sessionManagerURL**: Use data-session-manager-url
  ([`b9cbd68`](https://github.com/snacksbro/trame-client/commit/b9cbd68729917637dfcad9437506e54c00d50c09))

- **SharedArrayBuffer**: Disable by default service worker
  ([`92e0659`](https://github.com/snacksbro/trame-client/commit/92e0659457dc31b22806e14e4c2406d2f86fd4c6))

- **SizeObserver**: New network don't properly handle native js type
  ([`d9f9871`](https://github.com/snacksbro/trame-client/commit/d9f9871714661b6932070ca7060d4eb3ddcfa753))

- **state**: Ensure flush to not skip pending change
  ([`73694c5`](https://github.com/snacksbro/trame-client/commit/73694c5a9e58da8e5689a85a10af5bf110008f9c))

- **state**: Local change don't need server round trip
  ([`4eba70d`](https://github.com/snacksbro/trame-client/commit/4eba70d3b0867e5d0c02c5fc34e46dc098e64c4a))

- **state**: Prevent equal value to trigger change
  ([`8ab648d`](https://github.com/snacksbro/trame-client/commit/8ab648ddc4ab14140ccccded5892c6d285c850e3))

- **state**: Properly handle _filter after reload
  ([`c43046b`](https://github.com/snacksbro/trame-client/commit/c43046b2e6f2387655be6e54fca183b904b68ee4))

- **Style**: Add wwidget.client.Style widget to add custom css
  ([`48d0e0c`](https://github.com/snacksbro/trame-client/commit/48d0e0c4e115192be946c8667ba27a5a7c93e50b))

- **template**: Allow template name with underscore
  ([`dedd0aa`](https://github.com/snacksbro/trame-client/commit/dedd0aa413ee1adeb51d9df7c72e72ae00c941ec))

replace underscore with - to be vue.js compatible

fix #465

- **Template**: Expose it in widgets.html
  ([`ea90cc4`](https://github.com/snacksbro/trame-client/commit/ea90cc4e4acc9517f0d89ce5a0b354dc134ac1c0))

- **template**: Properly template name mapping
  ([`589991f`](https://github.com/snacksbro/trame-client/commit/589991fb086d3cadb9f8e9da1ccc6f848d342dfc))

- **test**: Fix test helpers for Windows
  ([`cd4b0d4`](https://github.com/snacksbro/trame-client/commit/cd4b0d4496b7d83be3c879d9b036b52a630eae1d))

* Use full current python path when running Selenium server python process * Fix port parsing in
  xprocess logs for Windows * Add option to disable log prints to avoid test clutter

- **testing**: Add more testing helper
  ([`c5a4d9c`](https://github.com/snacksbro/trame-client/commit/c5a4d9cd1f60f170a8250613cba9c5b87dc22e99))

- **testing**: Add testing utilities
  ([`a1c9c5c`](https://github.com/snacksbro/trame-client/commit/a1c9c5c980f5a4b37b2c1b6d024ad39aa493c683))

- **testing**: Add utilities functions
  ([`68c8509`](https://github.com/snacksbro/trame-client/commit/68c8509540bfc460919b3e478a323ada1e68ce44))

- **testing**: Allow enable_testing to be used as decorator
  ([`ce6f784`](https://github.com/snacksbro/trame-client/commit/ce6f784bb7a5681efe05359434f89c40b2a795a4))

- **text**: Fix error message text grammar
  ([`911259f`](https://github.com/snacksbro/trame-client/commit/911259fcfa17f2a093bfc4685c1abc7573a56f5f))

- **translation**: Auto translate state names in event too
  ([`46a2c74`](https://github.com/snacksbro/trame-client/commit/46a2c74155cdb3046633a1ce424b39c69b552f70))

- **translation**: Proper type handling with state translation
  ([`37b0e08`](https://github.com/snacksbro/trame-client/commit/37b0e08b17a115b8137b320acde9ff7750edbc27))

- **trigger**: Access client via `this.client`
  ([`9963d32`](https://github.com/snacksbro/trame-client/commit/9963d32555ab783c462833bf6776501e3bf56b60))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **trigger**: Add decorator logic for file objects
  ([`05235d5`](https://github.com/snacksbro/trame-client/commit/05235d514d707231632cdf83315c83d4bc0a04e2))

This is needed for the triggers to work properly with the file objects.

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **trigger**: Apply decorators on args/kwargs
  ([`8a3971a`](https://github.com/snacksbro/trame-client/commit/8a3971ad62a64b9e07dc7bc58acbd893cdc6ee9b))

- **use_**: Fix case sensitivity of use_host(name)
  ([`78c4bfd`](https://github.com/snacksbro/trame-client/commit/78c4bfd85277ad05bc2955233b3e13c1e7386ca8))

- **version**: Add trame_client.__version__
  ([`0b970b5`](https://github.com/snacksbro/trame-client/commit/0b970b562df52b8d8c2f26ac08cbec1d171ef9ba))

The `get_version()` function added here will also be used in all other trame-* packages.

Partially addresses Kitware/trame#183

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **virtual-node**: Follow builder pattern when possible
  ([`d0a5ce8`](https://github.com/snacksbro/trame-client/commit/d0a5ce867c999675e57008b3005e17f0b813282f))

- **vue2**: Rename components to match vue3 trame ones
  ([`ae98400`](https://github.com/snacksbro/trame-client/commit/ae98400cd747b4279bf03202e96f2cf30cb9585b))

- **vue2-app**: Fix URL params reading
  ([`0a6d33a`](https://github.com/snacksbro/trame-client/commit/0a6d33a579e195d7298d4a959755d9d8e32a83c9))

- **vue2.7**: Include composition API in vue2
  ([`ead4c74`](https://github.com/snacksbro/trame-client/commit/ead4c748b65c56d3809385ffc8672fc0abc55717))

- **vue2/3**: Parity
  ([`0d91ded`](https://github.com/snacksbro/trame-client/commit/0d91ded312523ad05f6438fa5265cd41accca6fb))

- **vue3**: Add support for ref/js_call
  ([`ec983ff`](https://github.com/snacksbro/trame-client/commit/ec983ff6c5ee3f869673c3de1d175732bff3f184))

- **vue3**: Destruct from window
  ([`9350e37`](https://github.com/snacksbro/trame-client/commit/9350e371625bd17ee11c3cf3157db63cc8f3c7a8))

- **vue3**: Fix client update for client_only props
  ([`093cecd`](https://github.com/snacksbro/trame-client/commit/093cecdaceb2d25804c273586dbc1a459739db52))

- **vue3**: Fix vue3 components remounting every time a key is added to state
  ([`417a71f`](https://github.com/snacksbro/trame-client/commit/417a71f12993f19c6142fcf64d657d7026ab21b7))

- **vue3**: Getter helper is now working
  ([`0008761`](https://github.com/snacksbro/trame-client/commit/00087613a6d9e5c408b39bdb4e74a3ad4e7ed4c5))

- **vue3**: Keep template syntax similar to vue2
  ([`c6778bc`](https://github.com/snacksbro/trame-client/commit/c6778bc33e82849b175128b02626cafb6bdfd698))

- **WebModule**: Add helper for serving web content
  ([`501caec`](https://github.com/snacksbro/trame-client/commit/501caec55d65a34e62583dadf519726aa4944e3f))

- **widget**: Add getter/setter definition
  ([`3aced83`](https://github.com/snacksbro/trame-client/commit/3aced83117b50194b813cb6b91a7d3396211866f))

- **wslink**: Simplify file upload helper by removing chunking
  ([`f87d8de`](https://github.com/snacksbro/trame-client/commit/f87d8deeaec8e80ecd0964d1c6e5c232155a998a))

BREAKING CHANGE: this requires the new chunking wslink

- **wslink**: Update version to support relative sessionManagerURL
  ([`2e62e57`](https://github.com/snacksbro/trame-client/commit/2e62e578603819fa336b259b6df3a61b192a9ca0))

### Chores

- Run black
  ([`ab221ea`](https://github.com/snacksbro/trame-client/commit/ab221ea3fe36310b85f8fee9c6ae43f80bf9b362))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **decorators**: Update fileHandler decorators in vue2/js-lib
  ([`0a23180`](https://github.com/snacksbro/trame-client/commit/0a231806a97aef8419124b47248da7668d15ac3d))

To match the changes made in 114a75e671d7ea80eae1d5c0fc75bb4c6d6820c2

- **js**: Add type definitions to js-lib
  ([`d2512ff`](https://github.com/snacksbro/trame-client/commit/d2512ff681c54d920dea7f3a6e7ce9b5164b1922))

- **js**: Advance @kitware/trame to v1.0.0
  ([`b558e1d`](https://github.com/snacksbro/trame-client/commit/b558e1d27b2e4dd409a6fad3f5caa20cba084bef))

- **js**: Remove vtk.js dependency from js-lib
  ([`ba2b813`](https://github.com/snacksbro/trame-client/commit/ba2b8133824ae449344a7ba000ffa97ae850e04b))

- **js-lib**: Add starting point
  ([`6f64052`](https://github.com/snacksbro/trame-client/commit/6f64052baba5055bac27e21c0a4c68c8e8617451))

- **js-lib**: Update version
  ([`2358431`](https://github.com/snacksbro/trame-client/commit/23584311eb07c2c79e08db24d536c63d9438f7c7))

- **semantic-release**: Bump version to latest
  ([`5e05792`](https://github.com/snacksbro/trame-client/commit/5e057928c2b3ecb04e53beb4bb911940cb494514))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

### Code Style

- **vue2**: Lint code
  ([`55389c7`](https://github.com/snacksbro/trame-client/commit/55389c749c1a8f6b4474b7b646e00b2ae0d99b7f))

### Continuous Integration

- Bring back testing
  ([`8bc7168`](https://github.com/snacksbro/trame-client/commit/8bc71686ec06fca425b90e1624148af6ad78c7b5))

- Disable test due to cross version dep
  ([`aabb2de`](https://github.com/snacksbro/trame-client/commit/aabb2de28727617370dfe30142c98b4b06187c9b))

- Fix precommit issues
  ([`56ee21d`](https://github.com/snacksbro/trame-client/commit/56ee21dde68abe32ac0ee6b272ba90b86f090ac7))

- Skip changelog for codespell
  ([`15c968d`](https://github.com/snacksbro/trame-client/commit/15c968d798a022534c3ee9b26ca2e90bf54b7721))

- **codespell**: Skip public/*.js
  ([`2c9533a`](https://github.com/snacksbro/trame-client/commit/2c9533a00292b3420497db7ba3fdf10d74d2d5ba))

- **codespell**: Utils/vtk/index.js for pixelX
  ([`463e2bd`](https://github.com/snacksbro/trame-client/commit/463e2bdfe5f931b99088a63a7ec92570501f256b))

- **js-lib**: Add missing new keyword
  ([`0a1bf78`](https://github.com/snacksbro/trame-client/commit/0a1bf78a06c09bb1ab7bbfabe08806d39eae694e))

- **js-lib**: Auto publish
  ([`4d6cc61`](https://github.com/snacksbro/trame-client/commit/4d6cc61f388afed1ab4ae2e4c72db7b6a9c660ad))

- **js-lib**: Bump version to rename exported object
  ([`557d1c4`](https://github.com/snacksbro/trame-client/commit/557d1c447d0b05ea6d459429c2f20859abb3ef01))

- **js-lib**: Fix publication automation
  ([`539f09f`](https://github.com/snacksbro/trame-client/commit/539f09feb7b6b25bb2b22fbc46f51a1c116084d6))

- **js-lib**: Try publishing library
  ([`c877746`](https://github.com/snacksbro/trame-client/commit/c87774612da7f307f45c614714572046cc807a1f))

- **playwright**: Use playwright for tests instead of selenium
  ([`cdd2e01`](https://github.com/snacksbro/trame-client/commit/cdd2e01e6e98defaac0a4aa555f17b7f6c21ca61))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **selenium**: Add dependencies
  ([`5524dc5`](https://github.com/snacksbro/trame-client/commit/5524dc5c23b6829f882a86fbfb9139d67e374b16))

- **server**: Better management of port extract
  ([`2ce2c25`](https://github.com/snacksbro/trame-client/commit/2ce2c25e8b30182605bf7084fcbaa906458b3c44))

- **test**: Add selenium test
  ([`28657da`](https://github.com/snacksbro/trame-client/commit/28657da68e25df057b3e10a2abc25aeb945a5333))

- **test**: Add trame as dependency
  ([`03b4e3b`](https://github.com/snacksbro/trame-client/commit/03b4e3b195153085a368c801ef6cec65885746c3))

- **test**: Explicitly use window
  ([`b57a62a`](https://github.com/snacksbro/trame-client/commit/b57a62a43d5c56f42135f50d4b2bc26b034f992f))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **test**: Remove vue3 tts validation
  ([`0c814d1`](https://github.com/snacksbro/trame-client/commit/0c814d16f41c857edcd995125a5a74c64d64d75e))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **tests**: Add back tts test
  ([`85e8d9a`](https://github.com/snacksbro/trame-client/commit/85e8d9ac67073c2622a7e813838eb730bf8cb1bd))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **tests**: Add ref/js_call testing
  ([`36de070`](https://github.com/snacksbro/trame-client/commit/36de07075cc36d26de38484b74d9a7fc14708252))

- **tests**: Add trame-server as a dependency
  ([`ed23fc4`](https://github.com/snacksbro/trame-client/commit/ed23fc4abf481d8d46f835b450d9fd4946b88385))

- **tests**: Build vue components before running tests
  ([`d1b7039`](https://github.com/snacksbro/trame-client/commit/d1b70391c29b32d84624e09a9bf93def4ff01822))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **tests**: Comment out failing tests for now
  ([`2ec90a3`](https://github.com/snacksbro/trame-client/commit/2ec90a3750d5f2e7dd6fd7c8c6584111f3613a4f))

We should fix these soon, though.

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **vue2/3**: Update path
  ([`fdb9c43`](https://github.com/snacksbro/trame-client/commit/fdb9c4306363ee22d4d56d2e54d070b21858fce1))

### Documentation

- Update links in readme
  ([`8e3e204`](https://github.com/snacksbro/trame-client/commit/8e3e2042214fd238b628216bff48d1762adf50a3))

- Update README.rst
  ([`2e75d47`](https://github.com/snacksbro/trame-client/commit/2e75d47533b545c2f2cbfb27a538468f15242b9b))

- **api**: Add missing information
  ([`f0a7d64`](https://github.com/snacksbro/trame-client/commit/f0a7d64d0f86365b47ae7a81a8596eb02a81e59a))

- **api**: Add missing information
  ([`857238f`](https://github.com/snacksbro/trame-client/commit/857238ff609b7636212c11bccd3c49bc0f31375b))

- **api**: Add missing information
  ([`b341015`](https://github.com/snacksbro/trame-client/commit/b341015f4625653a78ece1ffa3979eef6e1bf926))

- **ci**: Add coverage and codecov upload
  ([`c90ed26`](https://github.com/snacksbro/trame-client/commit/c90ed264f99cb29c92ad7cb191ed3690a1560f29))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **contributing**: Add CONTRIBUTING.rst
  ([`ad214da`](https://github.com/snacksbro/trame-client/commit/ad214da65ac48b298f592fe98591379110926486))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **coverage**: Add .coveragerc
  ([`f451bad`](https://github.com/snacksbro/trame-client/commit/f451bad3c73ac6791ab78ced92bbab1f7eb9751e))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **coverage**: Remove codecov PR comment
  ([`e9b0d9b`](https://github.com/snacksbro/trame-client/commit/e9b0d9b96346f694559a6077e7408d6899efe976))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **example**: Add client widgets example
  ([`e81909f`](https://github.com/snacksbro/trame-client/commit/e81909fff5775b673b3eb491c95761bea615a5a2))

- **example**: Make dynamic template hot reloadable
  ([`9dc58d4`](https://github.com/snacksbro/trame-client/commit/9dc58d4ebf37cfd12b36a86e383f707eab73b2ea))

- **examples**: Update vue3 template without .value
  ([`276c389`](https://github.com/snacksbro/trame-client/commit/276c3894ba1b28830d6268b681e0dd02aa83f88f))

- **js**: Add doc string to JS API
  ([`5c81263`](https://github.com/snacksbro/trame-client/commit/5c81263670063a915c1c3a2a1e8c1df35ac63ea1))

- **js**: List JS dependency
  ([`c87fa89`](https://github.com/snacksbro/trame-client/commit/c87fa89d6b7fccded0095ae5bdcec49fcaa95242))

- **js-lib**: Fix vite example
  ([`cc8ef8f`](https://github.com/snacksbro/trame-client/commit/cc8ef8f845b352326cda6ca0f56f232788c376b8))

- **js-lib**: Update library to fix js-doc annotation
  ([`533fbfd`](https://github.com/snacksbro/trame-client/commit/533fbfd3b50c3e1ba01208c42b3c66497356aba2))

- **readme**: Add CI badge
  ([`77cafe2`](https://github.com/snacksbro/trame-client/commit/77cafe24155e9d225b52f0abfd2ae086e8539155))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **readme**: Cleanup for vue2-3
  ([`3846b2c`](https://github.com/snacksbro/trame-client/commit/3846b2c25dc4cf78b1d0a2195fe4ff1cc10dbad2))

### Features

- **client**: Add ClientStateChange/ClientTriggers/LifeCycleMonitor/SizeObserver
  ([`5fa7fcf`](https://github.com/snacksbro/trame-client/commit/5fa7fcfea4b5111ca9d60ac732b810cec803e52d))

- **connect_parent**: Add flag to disable auto widget connection
  ([`5ef388f`](https://github.com/snacksbro/trame-client/commit/5ef388f972d6dec2ee115f833a8f580681a15409))

- **decorator**: Implement file chunking to prevent size limit
  ([`171a787`](https://github.com/snacksbro/trame-client/commit/171a78779deea3d5d02651cc9dff0cf6aabb7cab))

- **decorators**: Add new error key to uploaded file objects
  ([`7952155`](https://github.com/snacksbro/trame-client/commit/79521555eb91cd628bb1fa66b15ff2f69d802aaa))

Used so files with read errors don't halt execution, instead are handled gracefully and submitted to
  the server

- **DeepReactive**: Add vue3 component to enable deep reactivity
  ([`3ea4dc9`](https://github.com/snacksbro/trame-client/commit/3ea4dc94a0cc8fd8515c5f5b1ce2c19dfb0d81ba))

- **html**: Update html/vue available components
  ([`b3652d2`](https://github.com/snacksbro/trame-client/commit/b3652d296da0652004ce5f1e8c18657dfa866751))

- **install**: Generator json files dependency optional for runtime
  ([`9312181`](https://github.com/snacksbro/trame-client/commit/93121815d0b2c09256783efa2a62d03f7b8b9dd2))

- **jupyter**: Add display support for layouts
  ([`5373ac8`](https://github.com/snacksbro/trame-client/commit/5373ac8f63df9707c2813a5f36976fe0aecc7d8c))

- **jupyter**: Add support for jupyter extension
  ([`6d2bc50`](https://github.com/snacksbro/trame-client/commit/6d2bc50929128acd084580769797b2059ab4a56c))

- **launcher**: Enable retry option on launcher
  ([`8b1ae2d`](https://github.com/snacksbro/trame-client/commit/8b1ae2dbc6b621c92f75d53843b61031e8a925d7))

- **loading**: Enable loading screen to be overriden
  ([`9d13b21`](https://github.com/snacksbro/trame-client/commit/9d13b21a7bc99feef6621c1c538f7bb505282616))

For that just provide your own ./loading/index.html

Then in vue3, you can also override dynamically the error view for disconnect or
  disconnect-with-reconnect. You just need to define layout for "error" and "error_reconnect". Also
  a variable "trame_error_report_msg" will be available for you to leverage in your custom template.

- **raw_attrs**: Widgets support raw_attrs at construction
  ([`131618a`](https://github.com/snacksbro/trame-client/commit/131618a76f8d910e4007d14f6dc798a01d49da7d))

- **Reconnect**: Add support for reconnection
  ([`45a3b20`](https://github.com/snacksbro/trame-client/commit/45a3b2040bead26da83cde8b5bb51cd8423f59ff))

If you add ?reconnect in the URL, you will get a button to let you try to reconnect. If you add
  ?reconnect=auto in the URL, the client will try to reconnect automatically and stop after 10
  attempts.

- **repr**: Pretty print
  ([`2159799`](https://github.com/snacksbro/trame-client/commit/215979995e465b12dc5f0d4ab7c04e2bd1670e0f))

- **SharedArrayBuffer**: Enable by default while adding a disable option
  ([`49df5ed`](https://github.com/snacksbro/trame-client/commit/49df5edc52518c4eba918d81074b219d1e7c5e3e))

- **TrameComponent**: Provide helper class to handle method decoration
  ([`53390eb`](https://github.com/snacksbro/trame-client/commit/53390eb5178c8503b281da8298be58109ae750b3))

- **translator**: Template patching via translator
  ([`350bd63`](https://github.com/snacksbro/trame-client/commit/350bd63a22d45c4c5f6e9b5df8fd91d3fb4c4091))

- **url**: Can request url on layout when server started as task
  ([`f0584c1`](https://github.com/snacksbro/trame-client/commit/f0584c1e4ccb7d0971107a4b5e0a3577234347f7))

- **utils.tree**: Add helper to convert obj for VTreeview
  ([`f78edd9`](https://github.com/snacksbro/trame-client/commit/f78edd9311dbbba4fbf9773f7cce5970dd26f79f))

- **v_on**: Better handling events modifiers
  ([`942cbe3`](https://github.com/snacksbro/trame-client/commit/942cbe358772ed10d5a577fb087b01851e779cbd))

- **VirtualNode**: Introduce the virtual node concept
  ([`e1585ed`](https://github.com/snacksbro/trame-client/commit/e1585ed09b0e4bc1076a9f1e608ad0426a60925b))

- **vue2**: Add support for module scripts
  ([`9535d20`](https://github.com/snacksbro/trame-client/commit/9535d205b486a7a65f997cebdfff1b0c9bac31c2))

- **vue2**: Properly expose vue 2.7.14 for composition API
  ([`0371a12`](https://github.com/snacksbro/trame-client/commit/0371a12db5f49bef616faed2bc86050c20dcb450))

- **vue3**: Add state.watch API ([#29](https://github.com/snacksbro/trame-client/pull/29),
  [`d36a844`](https://github.com/snacksbro/trame-client/commit/d36a8447367a58464f4149bea808aaa996ce6b35))

- **vue3**: Add support for vue@3
  ([`423599b`](https://github.com/snacksbro/trame-client/commit/423599bbb6a64fb93b837814442e1d2c14a73354))

- **vue3**: Update vue version to latest
  ([`d49445c`](https://github.com/snacksbro/trame-client/commit/d49445cebd89cfa2dca723c78ca96ba4e689e16c))

- **vue3**: Update vue.js to v3.5.13
  ([`acdb5f0`](https://github.com/snacksbro/trame-client/commit/acdb5f00181e113b127d7765e39655b5392b8988))

Co-authored-by: Justine Antoine <justine.antoine@kitware.com>

- **widget**: Add state/ctrl/context property
  ([`d12b475`](https://github.com/snacksbro/trame-client/commit/d12b4751239f63be389cd13f319c467262206f6f))

- **widget**: Allow style attr to be dict
  ([`11f4ca5`](https://github.com/snacksbro/trame-client/commit/11f4ca504e0a64e198cbc2ec1fdcb62eb6295129))

- **widget**: Remove attribute when setting to None
  ([`2f827cb`](https://github.com/snacksbro/trame-client/commit/2f827cb6b22a5b86ec15baf6802f151be4caac95))

- **wslink**: Use msgpack and chunking for ws data exchange
  ([`77e17f5`](https://github.com/snacksbro/trame-client/commit/77e17f523ec912c16cd85376dc89d4e5ecdee5ab))

BREAKING CHANGE: use wslink>=2 that deeply change network handling

### Testing

- **translator**: Improve Translator tests
  ([`d7c99f7`](https://github.com/snacksbro/trame-client/commit/d7c99f76fe38d2701391110213ef41b144b34d92))
