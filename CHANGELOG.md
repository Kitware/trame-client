# Changelog

<!--next-version-placeholder-->

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
