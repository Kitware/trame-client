# Changelog

<!--next-version-placeholder-->

## v2.7.5 (2023-03-27)
### Fix
* **kwargs:** Fix handling of vue3 of kwargs ([`2e8815e`](https://github.com/Kitware/trame-client/commit/2e8815e3ff8c4e853417128714a1103c585d3da2))
* **kwargs:** Fix handling of vue2 of kwargs ([`28c463e`](https://github.com/Kitware/trame-client/commit/28c463e68f1faf306ed5fa89c0e62e7dcd439549))

### Documentation
* **example:** Make dynamic template hot reloadable ([`9dc58d4`](https://github.com/Kitware/trame-client/commit/9dc58d4ebf37cfd12b36a86e383f707eab73b2ea))

## v2.7.4 (2023-03-06)
### Fix
* **html:** Add v-slot and v-model modifier ([`1863cc0`](https://github.com/Kitware/trame-client/commit/1863cc0cf5330c7bde9207787701d871cd019ec0))

## v2.7.3 (2023-02-26)
### Fix
* **vue3:** Destruct from window ([`9350e37`](https://github.com/Kitware/trame-client/commit/9350e371625bd17ee11c3cf3157db63cc8f3c7a8))

## v2.7.2 (2023-02-26)
### Fix
* **vue3:** Keep template syntax similar to vue2 ([`c6778bc`](https://github.com/Kitware/trame-client/commit/c6778bc33e82849b175128b02626cafb6bdfd698))

### Documentation
* **examples:** Update vue3 template without .value ([`276c389`](https://github.com/Kitware/trame-client/commit/276c3894ba1b28830d6268b681e0dd02aa83f88f))

## v2.7.1 (2023-02-22)
### Fix
* **layout:** Keep track of the original root ([`66355b3`](https://github.com/Kitware/trame-client/commit/66355b30e75f7c28937b4d9a41fd939bd8812024))

## v2.7.0 (2023-02-14)
### Feature
* **vue2:** Properly expose vue 2.7.14 for composition API ([`0371a12`](https://github.com/Kitware/trame-client/commit/0371a12db5f49bef616faed2bc86050c20dcb450))

## v2.6.3 (2023-02-13)
### Fix
* **vue2.7:** Include composition API in vue2 ([`ead4c74`](https://github.com/Kitware/trame-client/commit/ead4c748b65c56d3809385ffc8672fc0abc55717))

## v2.6.2 (2023-02-13)
### Fix
* **vue3:** Add support for ref/js_call ([`ec983ff`](https://github.com/Kitware/trame-client/commit/ec983ff6c5ee3f869673c3de1d175732bff3f184))

### Documentation
* **readme:** Cleanup for vue2-3 ([`3846b2c`](https://github.com/Kitware/trame-client/commit/3846b2c25dc4cf78b1d0a2195fe4ff1cc10dbad2))

## v2.6.1 (2023-02-11)
### Fix
* **vue3:** Fix client update for client_only props ([`093cecd`](https://github.com/Kitware/trame-client/commit/093cecdaceb2d25804c273586dbc1a459739db52))
* **default-var:** Allow right default to be a dict to update many vars ([`ca7a5dc`](https://github.com/Kitware/trame-client/commit/ca7a5dc96332aa229e1a97f62b003ad69090c395))

## v2.6.0 (2023-02-09)
### Feature
* **vue3:** Add support for vue@3 ([`423599b`](https://github.com/Kitware/trame-client/commit/423599bbb6a64fb93b837814442e1d2c14a73354))

### Fix
* **py:** Removed unused component from Python ([`d581e43`](https://github.com/Kitware/trame-client/commit/d581e432ecffed7a1e325276ac5da3c7bf087e0e))
* **vue2:** Rename components to match vue3 trame ones ([`ae98400`](https://github.com/Kitware/trame-client/commit/ae98400cd747b4279bf03202e96f2cf30cb9585b))
* **vue2/3:** Parity ([`0d91ded`](https://github.com/Kitware/trame-client/commit/0d91ded312523ad05f6438fa5265cd41accca6fb))
* **refs:** Start on js_call/ref handling ([`3aa2c53`](https://github.com/Kitware/trame-client/commit/3aa2c531cc4ed20773d5f83cb6ae95a7169f3e47))

### Documentation
* **example:** Add client widgets example ([`e81909f`](https://github.com/Kitware/trame-client/commit/e81909fff5775b673b3eb491c95761bea615a5a2))

## v2.5.1 (2023-01-27)
### Fix
* **version:** Add trame_client.__version__ ([`0b970b5`](https://github.com/Kitware/trame-client/commit/0b970b562df52b8d8c2f26ac08cbec1d171ef9ba))

## v2.5.0 (2023-01-23)
### Feature
* **utils.tree:** Add helper to convert obj for VTreeview ([`f78edd9`](https://github.com/Kitware/trame-client/commit/f78edd9311dbbba4fbf9773f7cce5970dd26f79f))

## v2.4.2 (2023-01-19)
### Fix
* **text:** Fix error message text grammar ([`911259f`](https://github.com/Kitware/trame-client/commit/911259fcfa17f2a093bfc4685c1abc7573a56f5f))

## v2.4.1 (2023-01-13)
### Fix
* **Reconnect:** Allow template name to be used ([`3cad023`](https://github.com/Kitware/trame-client/commit/3cad0237582f46fe0f46e726b5fa1d9b71812f6b))

## v2.4.0 (2022-12-18)
### Feature
* **Reconnect:** Add support for reconnection ([`45a3b20`](https://github.com/Kitware/trame-client/commit/45a3b2040bead26da83cde8b5bb51cd8423f59ff))

### Fix
* **cache:** Try to prevent web caching ([`2bb25a0`](https://github.com/Kitware/trame-client/commit/2bb25a0a6e8a1e42b3bfe7c652a0c59b375e540d))

## v2.3.6 (2022-12-12)
### Fix
* **trigger:** Access client via `this.client` ([`9963d32`](https://github.com/Kitware/trame-client/commit/9963d32555ab783c462833bf6776501e3bf56b60))

## v2.3.5 (2022-12-09)
### Fix
* **trigger:** Add decorator logic for file objects ([`05235d5`](https://github.com/Kitware/trame-client/commit/05235d514d707231632cdf83315c83d4bc0a04e2))

## v2.3.4 (2022-12-08)
### Fix
* **wslink:** Update version to support relative sessionManagerURL ([`2e62e57`](https://github.com/Kitware/trame-client/commit/2e62e578603819fa336b259b6df3a61b192a9ca0))
* **Style:** Add wwidget.client.Style widget to add custom css ([`48d0e0c`](https://github.com/Kitware/trame-client/commit/48d0e0c4e115192be946c8667ba27a5a7c93e50b))
* **trigger:** Apply decorators on args/kwargs ([`8a3971a`](https://github.com/Kitware/trame-client/commit/8a3971ad62a64b9e07dc7bc58acbd893cdc6ee9b))

## v2.3.3 (2022-12-07)
### Fix
* **sessionManagerURL:** Use data-session-manager-url ([`b9cbd68`](https://github.com/Kitware/trame-client/commit/b9cbd68729917637dfcad9437506e54c00d50c09))
* **sessionManagerURL:** Add option to read it from the html element dataset ([`7d174c4`](https://github.com/Kitware/trame-client/commit/7d174c4fbbe371eb59023da553305b1d9a6a52c0))

## v2.3.2 (2022-12-04)
### Fix
* **decorators:** Replace blob.arrayBuffer with backward-compatible code ([`439b50e`](https://github.com/Kitware/trame-client/commit/439b50eed98b58e1e8eaf25b7f0dd8042bf9ec3b))

## v2.3.1 (2022-11-08)
### Fix
* **protocol:** Update wslink for protocol resolution ([`12b64ab`](https://github.com/Kitware/trame-client/commit/12b64ab5972b32a835af08af2f3c3aa1529ebe64))

## v2.3.0 (2022-10-24)
### Feature
* **install:** Generator json files dependency optional for runtime ([`9312181`](https://github.com/Kitware/trame-client/commit/93121815d0b2c09256783efa2a62d03f7b8b9dd2))

## v2.2.2 (2022-10-21)
### Fix
* **state:** Ensure flush to not skip pending change ([`73694c5`](https://github.com/Kitware/trame-client/commit/73694c5a9e58da8e5689a85a10af5bf110008f9c))

## v2.2.1 (2022-10-20)
### Fix
* **state:** Local change don't need server round trip ([`4eba70d`](https://github.com/Kitware/trame-client/commit/4eba70d3b0867e5d0c02c5fc34e46dc098e64c4a))

## v2.2.0 (2022-08-29)
### Feature
* **decorator:** Implement file chunking to prevent size limit ([`171a787`](https://github.com/Kitware/trame-client/commit/171a78779deea3d5d02651cc9dff0cf6aabb7cab))

## v2.1.5 (2022-08-10)
### Fix
* **download:** Allow promise as content ([`87bc3d7`](https://github.com/Kitware/trame-client/commit/87bc3d7728b4ddca0a24b9466558583cc7fb224e))

### Documentation
* **coverage:** Remove codecov PR comment ([`e9b0d9b`](https://github.com/Kitware/trame-client/commit/e9b0d9b96346f694559a6077e7408d6899efe976))
* **coverage:** Add .coveragerc ([`f451bad`](https://github.com/Kitware/trame-client/commit/f451bad3c73ac6791ab78ced92bbab1f7eb9751e))
* **ci:** Add coverage and codecov upload ([`c90ed26`](https://github.com/Kitware/trame-client/commit/c90ed264f99cb29c92ad7cb191ed3690a1560f29))
* **readme:** Add CI badge ([`77cafe2`](https://github.com/Kitware/trame-client/commit/77cafe24155e9d225b52f0abfd2ae086e8539155))

## v2.1.4 (2022-06-19)
### Fix
* **virtual-node:** Follow builder pattern when possible ([`d0a5ce8`](https://github.com/Kitware/trame-client/commit/d0a5ce867c999675e57008b3005e17f0b813282f))

## v2.1.3 (2022-06-14)
### Fix
* **desktop:** Add edge 18 support ([`2238072`](https://github.com/Kitware/trame-client/commit/2238072e261a76315d4014dc236a0b1793671f3e))

## v2.1.2 (2022-06-14)
### Fix
* **cfe:** Add chrome 66 compatibility for cfe runtime ([`5dc7b5b`](https://github.com/Kitware/trame-client/commit/5dc7b5b6d7b0f58a461ca1dd2d3522d6d2d686e9))

## v2.1.1 (2022-06-10)
### Fix
* **state:** Prevent equal value to trigger change ([`8ab648d`](https://github.com/Kitware/trame-client/commit/8ab648ddc4ab14140ccccded5892c6d285c850e3))

### Documentation
* **contributing:** Add CONTRIBUTING.rst ([`ad214da`](https://github.com/Kitware/trame-client/commit/ad214da65ac48b298f592fe98591379110926486))

## v2.1.0 (2022-06-04)
### Feature
* **VirtualNode:** Introduce the virtual node concept ([`e1585ed`](https://github.com/Kitware/trame-client/commit/e1585ed09b0e4bc1076a9f1e608ad0426a60925b))

## v2.0.3 (2022-06-03)
### Fix
* **use_:** Fix case sensitivity of use_host(name) ([`78c4bfd`](https://github.com/Kitware/trame-client/commit/78c4bfd85277ad05bc2955233b3e13c1e7386ca8))

## v2.0.2 (2022-05-30)
### Fix
* **state:** Properly handle _filter after reload ([`c43046b`](https://github.com/Kitware/trame-client/commit/c43046b2e6f2387655be6e54fca183b904b68ee4))

## v2.0.1 (2022-05-27)
### Fix
* **CI:** Add initial CI with semantic-release ([`51323fd`](https://github.com/Kitware/trame-client/commit/51323fdcbd9e519dfa594948557cbaf6b30c88ac))
* **client:** Latest client build ([`cfef0b4`](https://github.com/Kitware/trame-client/commit/cfef0b4c58a462e2f378bf27a89468b20c3679d6))
* **Template:** Expose it in widgets.html ([`ea90cc4`](https://github.com/Kitware/trame-client/commit/ea90cc4e4acc9517f0d89ce5a0b354dc134ac1c0))

### Documentation
* **api:** Add missing information ([`f0a7d64`](https://github.com/Kitware/trame-client/commit/f0a7d64d0f86365b47ae7a81a8596eb02a81e59a))
* **api:** Add missing information ([`857238f`](https://github.com/Kitware/trame-client/commit/857238ff609b7636212c11bccd3c49bc0f31375b))
* **api:** Add missing information ([`b341015`](https://github.com/Kitware/trame-client/commit/b341015f4625653a78ece1ffa3979eef6e1bf926))
