# Event

## useq.MDAEvent

Bases: `UseqModel`

Define a single event in a `MDASequence`.

Usually, this object will be generator by iterating over a `MDASequence` (see `useq.MDASequence.iter_events`).

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

<table>       <thead>         <tr>           <th>Name</th>           <th>Type</th>           <th>Description</th>           <th>Default</th>         </tr>       </thead>       <tbody>           <tr class="doc-section-item">             <td>                 <code>index</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" hover="" identifier="useq._mda_event.ReadOnlyDict" optional="">ReadOnlyDict</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p>A read-only dictionary.</p>                </div>             </td>             <td>                   <code>&lt;dynamic&gt;</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>channel</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" hover="" identifier="useq._mda_event.Channel" optional="">Channel</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>exposure</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="float" optional="">float</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>min_start_time</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="float" optional="">float</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>pos_name</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="str" optional="">str</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>x_pos</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="float" optional="">float</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>y_pos</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="float" optional="">float</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>z_pos</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="float" optional="">float</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>slm_image</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" hover="" identifier="useq._mda_event.SLMImage" optional="">SLMImage</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>sequence</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" hover="" identifier="useq._mda_sequence.MDASequence" optional="">MDASequence</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>properties</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="list" optional="">list</autoref>[<autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" hover="" identifier="useq._mda_event.PropertyTuple" optional="">PropertyTuple</autoref>] | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>roi</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" hover="" identifier="useq._mda_event.CameraROI" optional="">CameraROI</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>metadata</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="dict" optional="">dict</autoref>[<autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="str" optional="">str</autoref>, <autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" hover="" identifier="typing.Any" optional="">Any</autoref>]</code>             </td>             <td>               <div class="doc-md-description">                 <p>dict() -&gt; new empty dictionary dict(mapping) -&gt; new dictionary initialized from a mapping object's     (key, value) pairs dict(iterable) -&gt; new dictionary initialized as if via:     d = {}     for k, v in iterable:         d[k] = v dict(**kwargs) -&gt; new dictionary initialized with the name=value pairs     in the keyword argument list.  For example:  dict(one=1, two=2)</p>                </div>             </td>             <td>                   <code>&lt;class 'dict'&gt;</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>action</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" hover="" identifier="useq._actions.HardwareAutofocus" optional="">HardwareAutofocus</autoref> | <autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" hover="" identifier="useq._actions.AcquireImage" optional="">AcquireImage</autoref> | <autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" hover="" identifier="useq._actions.CustomAction" optional="">CustomAction</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p><autoref data-zensical-autoref="" domain="py" filepath="/Users/runner/work/pymmcore-plus.github.io/pymmcore-plus.github.io/.repos/useq-schema/src/useq/_mda_event.py" identifier="useq.Action" lineno="214" origin="useq.MDAEvent" role="class"><code>useq.Action</code></autoref> to acquire an image.</p> <h4 id="useq.MDAEvent--attributes">Attributes</h4> <p>type : Literal[&quot;acquire_image&quot;]     This action can be used to acquire an image.</p>                </div>             </td>             <td>                   <code>&lt;dynamic&gt;</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>keep_shutter_open</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="bool" optional="">bool</autoref></code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>False</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>reset_event_timer</code>             </td>             <td>                   <code><autoref backlink-anchor="useq.MDAEvent" backlink-type="used-by" identifier="bool" optional="">bool</autoref></code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>             <td>                   <code>False</code>             </td>           </tr>       </tbody>     </table>

## useq.EventChannel

Bases: `UseqModel`

Channel in a MDA event.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `config` | `str` |  | *required* |
| `group` | `str` |  | `'Channel'` |

## useq.PropertyTuple

Bases: `NamedTuple`

Three-tuple capturing a device, property, and value.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `value` | `Any` | Value for the property. |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_name` | `str` |  | `None` |
| `property_name` | `str` |  | `None` |
| `property_value` | `Any` |  | `None` |

## Event Actions

## useq.Action

Bases: `FrozenModel`

Base class for a `useq.MDAEvent` action.

An `Action` specifies what task should be performed during a `useq.MDAEvent`. An `Action` can be for example used to acquire an image (`useq.AcquireImage`) or to perform a hardware autofocus (`useq.HardwareAutofocus`). An action of `None` implies `AcquireImage`.

You may use `CustomAction` to indicate any custom action, with the `data` attribute containing any data required to perform the custom action.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `type` | `str` |  | *required* |

## useq.AcquireImage

Bases: `Action`

`useq.Action` to acquire an image.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `type` | `Literal['acquire_image']` |  | `'acquire_image'` |

## useq.HardwareAutofocus

Bases: `Action`

`useq.Action` to perform a hardware autofocus.

See also `useq.AutoFocusPlan`.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `type` | `Literal['hardware_autofocus']` |  | `'hardware_autofocus'` |
| `autofocus_device_name` | `str \| None` |  | `None` |
| `autofocus_motor_offset` | `float \| None` |  | `None` |
| `max_retries` | `int` |  | `3` |

## useq.CustomAction

Bases: `Action`

`useq.Action` to perform a custom action.

This is a generic user action that can be used to represent anything that is not covered by the other action types, such as a microfluidic event, or a photostimulation, etc...

The `data` attribute is a dictionary that can contain any data that is needed to perform the custom action. It *must* be serializable to JSON by `pydantic`.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `type` | `Literal['custom']` |  | `'custom'` |
| `name` | `str` |  | `''` |
| `data` | `dict` | dict() -\> new empty dictionary dict(mapping) -\> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -\> new dictionary initialized as if via: d = {} for k, v in iterable: d\[k\] = v dict(\*\*kwargs) -\> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) | `<class 'dict'>` |
