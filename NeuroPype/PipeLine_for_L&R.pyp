<?xml version='1.0' encoding='utf-8'?>
<scheme description="This pipeline predicts imagined motor actions using neural oscillatory pattern classification. The main node of this pipeline is the Common Spatial Pattern (CSP) filter, which is used to retrieve the components or patterns in the signal that are most suitable to represent desired categories or classes. CSP and its various extensions (available through NeuroPype) provide a powerful tool for building applications based on neural oscillations.&#10;This pipeline can be divided into 4 main parts, which we discuss in the following:&#10;&#10;Data acquisition:&#10;Includes : Import Data (here titled “Import SET”), LSL input/output, Stream Data and Inject Calibration Data nodes.&#10;In general you can process your data online or offline. For developing and testing purposes you will be mostly performing offline process using a pre-recorded file.&#10;&#10;- The “Import Data” nodes (here titled “Import Set”) are used to connect the pipeline to files.&#10;&#10;- The “LSL input” and “LSL output” nodes are used to get data stream into the pipeline, or send the data out to the network from the pipeline. (If you are sending markers make sure to check the “send marker” option in “LSL output” node)&#10;&#10;- The “Inject Calibration Data” node is used to pass the initial calibration data into the pipeline before the actual data is processed. The calibration data (Calib Data) is used by adaptive and machine learning algorithms to train and set their parameters initially. The main data is connected to the “Streaming Data” port.&#10;&#10;NOTE regarding “Inject Calibration Data”: &#10;In case you would like to train and test your pipeline using files (without using streaming node), you need to set the “Delay streaming packets” in this node. This enables the “Inject Calibration Data” node to buffer the test data that is pushed into it for one cycle and transfer it to the output port in the next cycle. It should be noted that the first cycle is used to push the calibration data through the pipeline.&#10;&#10;Data preprocess:&#10;Includes: Assign Targets, Select Range,  FIR filter and Segmentation nodes&#10;&#10;- The “Assign Target” node is mostly useful for the supervised learning algorithms, where  target values are assigned to specific markers present in the EEG signal. In order for this node to operate correctly you need to know the label for the markers in the data.&#10;&#10;- The “Select Range” node is used to specify certain parts of the data stream. For example, if we have a headset that contains certain bad channels, you can manually remove them here. That is the case for our example here where only data from the last 6 channels are used.&#10;&#10;- The “FIR Filter” node is used to remove the unwanted signals components outside of the EEG signal frequencies, e.g. to keep the 6-30 Hz frequency window.&#10;&#10;- The “Segmentation” node performs the epoching process, where the streamed data is divided into segments of the predefined window-length around the markers on the EEG data.&#10;&#10;NOTE regarding &quot;Segmentation&quot; node:&#10;The epoching process can be either done relative to the marker or the time window. When Processing a large file you should set the epoching relative to markers and while processing the streaming data, you should set it to sliding which chooses a single window at the end of the data.&#10;&#10;Feature extraction:&#10;&#10;Includes: Common Spatial Patterns (CSP) node&#10;As discussed above the spectral and spatial patterns in the data can be extracted by the CSP filters and its extensions.&#10;&#10;Classification:&#10;Includes: Variance, Logarithm, Logistic Regression and Measure Loss&#10;&#10;- The “Logistic Regression” node is used to perform the classification, where supervised learning methods is used to train the classifier. in this node you can choose the type of regularization and the regularization coefficient. You can also set the number of the folds for cross-validation in this node.&#10;&#10;- The “Measure Loss” node is used to measure various performance criteria. Here we use misclassification rate (MCR)." title="Simple Motor Imagery Prediction with CSP" version="2.0">
	<nodes>
		<node id="0" name="Assign Target Values" position="(657.0, 469.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Targets" uuid="b49a17d8-c29f-457c-8d60-38177fbe88bf" version="1.0.1" />
		<node id="1" name="Segmentation" position="(1027.0, 553.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="ab15e38a-0308-4c99-8756-652b908e9dad" version="1.0.2" />
		<node id="2" name="Common Spatial Patterns" position="(1158.0, 482.0)" project_name="NeuroPype" qualified_name="widgets.neural.owcommonspatialpatterns.OWCommonSpatialPatterns" title="Common Spatial Patterns" uuid="257d6393-cd4f-471c-988a-c9d9f900e721" version="1.0.0" />
		<node id="3" name="Variance" position="(1296.0, 557.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="242f3894-14a6-4e10-b354-bf252110fd9f" version="1.0.0" />
		<node id="4" name="Logarithm" position="(1433.0, 484.0)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owlogarithm.OWLogarithm" title="Logarithm" uuid="bd42a46b-8342-450a-b7c8-c1ca5059473a" version="1.0.0" />
		<node id="5" name="Select Range" position="(773.0, 558.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="c1857f49-c2aa-4d75-976e-47c0792dc687" version="1.1.0" />
		<node id="6" name="Logistic Regression" position="(1554.0, 553.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression" uuid="07c44a21-942f-425e-90a6-e0630910562a" version="1.1.0" />
		<node id="7" name="FIR Filter" position="(882.0, 480.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="e151bea6-d740-4907-a4ee-6182747b7acd" version="1.1.0" />
		<node id="8" name="LSL Input" position="(118.0, 388.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="1aafd7dc-4182-4bb4-aadb-bf687638dd77" version="1.3.6" />
		<node id="9" name="Dejitter Timestamps" position="(296.0, 392.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="f334662f-e9c8-452a-868d-4e00a4574036" version="1.0.0" />
		<node id="10" name="Inject Calibration Data" position="(542.0, 512.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owinjectcalibrationdata.OWInjectCalibrationData" title="Inject Calibration Data" uuid="3d1b3a74-ff29-47a4-8ad9-9f3fc0c2652a" version="1.0.0" />
		<node id="11" name="Import XDF" position="(125.0, 514.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="2e59e739-de98-4f0a-bb81-8576111d3849" version="1.2.1" />
		<node id="12" name="OSC Output" position="(1708.0, 781.0)" project_name="NeuroPype" qualified_name="widgets.network.owoscoutput.OWOSCOutput" title="OSC Output" uuid="47db5d5f-8cb6-4988-a5bf-840d0ffa5f96" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="8" sink_channel="Streaming Data" sink_node_id="10" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="10" sink_channel="Calib Data" sink_node_id="10" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="6" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYBQAAAHJpZ2h0cQdL
AVgEAAAAbGVmdHEISwB1WA4AAABtYXBwaW5nX2Zvcm1hdHEJWAYAAABjb21wYXRxClgIAAAAbWV0
YWRhdGFxC31xDFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXENY3NpcApfdW5waWNrbGVfdHlwZQpx
DlgMAAAAUHlRdDUuUXRDb3JlcQ9YCgAAAFFCeXRlQXJyYXlxEENCAdnQywADAAAAAAOqAAACTAAA
BRMAAAMqAAADqwAAAnkAAAUSAAADKQAAAAAAAAAACNAAAAOrAAACeQAABRIAAAMpcRGFcRKHcRNS
cRRYDgAAAHNldF9icmVha3BvaW50cRWJWBEAAABzdXBwb3J0X3dpbGRjYXJkc3EWiVgLAAAAdXNl
X251bWJlcnNxF4lYBwAAAHZlcmJvc2VxGIl1Lg==
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgIAAAAbWV0YWRhdGFxA31xBFgPAAAAb25saW5lX2Vwb2NoaW5ncQVYBwAAAHNsaWRpbmdx
BlgNAAAAc2FtcGxlX29mZnNldHEHSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCGNzaXAKX3Vu
cGlja2xlX3R5cGUKcQlYDAAAAFB5UXQ1LlF0Q29yZXEKWAoAAABRQnl0ZUFycmF5cQtDQgHZ0MsA
AwAAAAAELwAAAzEAAAWYAAAEagAABDAAAANeAAAFlwAABGkAAAAAAAAAAAjQAAAEMAAAA14AAAWX
AAAEaXEMhXENh3EOUnEPWA4AAABzZWxlY3RfbWFya2Vyc3EQWA0AAAAodXNlIGRlZmF1bHQpcRFY
DgAAAHNldF9icmVha3BvaW50cRKJWAsAAAB0aW1lX2JvdW5kc3ETRz/gAAAAAAAAR0AMAAAAAAAA
hnEUWAcAAAB2ZXJib3NlcRWJdS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAoAAABjb25kX2ZpZWxkcQFYCwAAAFRhcmdldFZhbHVlcQJYDwAAAGluaXRpYWxpemVf
b25jZXEDiFgIAAAAbWV0YWRhdGFxBH1xBVgDAAAAbm9mcQZLAlgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXEHY3NpcApfdW5waWNrbGVfdHlwZQpxCFgMAAAAUHlRdDUuUXRDb3JlcQlYCgAAAFFCeXRl
QXJyYXlxCkNCAdnQywADAAAAAATOAAACzgAABkkAAAN0AAAEzwAAAvsAAAZIAAADcwAAAAAAAAAA
CNAAAATPAAAC+wAABkgAAANzcQuFcQyHcQ1ScQ5YDgAAAHNldF9icmVha3BvaW50cQ+JdS4=
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWAgAAABtZXRhZGF0YXEFfXEGWBMAAABzYXZlZFdpZGdl
dEdlb21ldHJ5cQdjc2lwCl91bnBpY2tsZV90eXBlCnEIWAwAAABQeVF0NS5RdENvcmVxCVgKAAAA
UUJ5dGVBcnJheXEKQ0IB2dDLAAMAAAAAA6oAAAJpAAAFEwAAAwwAAAOrAAAClgAABRIAAAMLAAAA
AAAAAAAI0AAAA6sAAAKWAAAFEgAAAwtxC4VxDIdxDVJxDlgOAAAAc2V0X2JyZWFrcG9pbnRxD4l1
Lg==
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAQAAABiYXNlcQFYDQAAACh1c2UgZGVmYXVsdClxAlgIAAAAbWV0YWRhdGFxA31xBFgT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNrbGVfdHlwZQpxBlgMAAAAUHlRdDUu
UXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCENCAdnQywADAAAAAAOqAAACaAAABRMAAAMOAAADqwAA
ApUAAAUSAAADDQAAAAAAAAAACNAAAAOrAAAClQAABRIAAAMNcQmFcQqHcQtScQxYDgAAAHNldF9i
cmVha3BvaW50cQ2JdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWB8AAABhcHBseV90aW1lX3NlbGVjdGlv
bl90b19tYXJrZXJzcQKJWAQAAABheGlzcQNYBQAAAHNwYWNlcQRYCAAAAG1ldGFkYXRhcQV9cQZY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxB2NzaXAKX3VucGlja2xlX3R5cGUKcQhYDAAAAFB5UXQ1
LlF0Q29yZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAADigAAAj0AAAUzAAADOAAAA4sA
AAJqAAAFMgAAAzcAAAAAAAAAAAjQAAADiwAAAmoAAAUyAAADN3ELhXEMh3ENUnEOWAkAAABzZWxl
Y3Rpb25xD1gDAAAAOi02cRBYDgAAAHNldF9icmVha3BvaW50cRGJWAQAAAB1bml0cRJYBwAAAGlu
ZGljZXNxE3Uu
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYBAAA
AGF1dG9xBVgKAAAAY29uZF9maWVsZHEGWAsAAABUYXJnZXRWYWx1ZXEHWBAAAABkb250X3Jlc2V0
X21vZGVscQiJWBAAAABkdWFsX2Zvcm11bGF0aW9ucQmJWA8AAABmZWF0dXJlX3NjYWxpbmdxClgE
AAAAbm9uZXELWAwAAABpbmNsdWRlX2JpYXNxDIhYDwAAAGluaXRpYWxpemVfb25jZXENiFgJAAAA
bDFfcmF0aW9zcQ5YDQAAACh1c2UgZGVmYXVsdClxD1gIAAAAbWF4X2l0ZXJxEEtkWAgAAABtZXRh
ZGF0YXERfXESWAoAAABtdWx0aWNsYXNzcRNYAwAAAG92cnEUWAkAAABudW1fZm9sZHNxFUsFWAgA
AABudW1fam9ic3EWSwFYDQAAAHByb2JhYmlsaXN0aWNxF4hYCwAAAHJhbmRvbV9zZWVkcRhNOTBY
CwAAAHJlZ3VsYXJpemVycRlYAgAAAGwycRpYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxG2NzaXAK
X3VucGlja2xlX3R5cGUKcRxYDAAAAFB5UXQ1LlF0Q29yZXEdWAoAAABRQnl0ZUFycmF5cR5DQgHZ
0MsAAwAAAAADowAAAiwAAAUbAAADSgAAA6QAAAJZAAAFGgAAA0kAAAAAAAAAAAjQAAADpAAAAlkA
AAUaAAADSXEfhXEgh3EhUnEiWA0AAABzZWFyY2hfbWV0cmljcSNYCAAAAGFjY3VyYWN5cSRYDgAA
AHNldF9icmVha3BvaW50cSWJWAYAAABzb2x2ZXJxJlgFAAAAbGJmZ3NxJ1gJAAAAdG9sZXJhbmNl
cShHPxo24uscQy1YCQAAAHZlcmJvc2l0eXEpSwB1Lg==
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsGSwdLHksgZVgIAAAAbWV0YWRhdGFxCX1xClgNAAAAbWluaW11
bV9waGFzZXELiFgEAAAAbW9kZXEMWAgAAABiYW5kcGFzc3ENWAUAAABvcmRlcnEOWA0AAAAodXNl
IGRlZmF1bHQpcQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlja2xlX3R5cGUK
cRFYDAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDQgHZ0MsAAwAAAAADqwAAAnkA
AAUSAAADKQAAA6sAAAJ5AAAFEgAAAykAAAAAAAAAAAjQAAADqwAAAnkAAAUSAAADKXEUhXEVh3EW
UnEXWA4AAABzZXRfYnJlYWtwb2ludHEYiVgKAAAAc3RvcF9hdHRlbnEZR0BJAAAAAAAAdS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgAAAAAcQlYDAAAAG1heF9ibG9ja2xlbnEKTQAEWAoAAABtYXhfYnVmbGVu
cQtLHlgMAAAAbWF4X2NodW5rbGVucQxLAFgIAAAAbWV0YWRhdGFxDX1xDlgMAAAAbm9taW5hbF9y
YXRlcQ9YDQAAACh1c2UgZGVmYXVsdClxEFgJAAAAb21pdF9kZXNjcRGJWA8AAABwcmVhbGxvY19i
dWZmZXJxEohYDgAAAHByb2NfY2xvY2tzeW5jcROIWA0AAABwcm9jX2Rlaml0dGVycRSJWA8AAABw
cm9jX21vbm90b25pemVxFYlYDwAAAHByb2NfdGhyZWFkc2FmZXEWiVgFAAAAcXVlcnlxF1gQAAAA
bmFtZT0nb2JjaV9lZWcxJ3EYWAcAAAByZWNvdmVycRmIWBQAAAByZXNvbHZlX21pbmltdW1fdGlt
ZXEaRz/gAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRtjc2lwCl91bnBpY2tsZV90eXBl
CnEcWAwAAABQeVF0NS5RdENvcmVxHVgKAAAAUUJ5dGVBcnJheXEeQ0IB2dDLAAMAAAAAA6QAAAHp
AAAFGgAAA4wAAAOlAAACFgAABRkAAAOLAAAAAAAAAAAI0AAAA6UAAAIWAAAFGQAAA4txH4VxIIdx
IVJxIlgOAAAAc2V0X2JyZWFrcG9pbnRxI4l1Lg==
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECTSwBWA4A
AABtYXhfdXBkYXRlcmF0ZXEDTfQBWAgAAABtZXRhZGF0YXEEfXEFWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cQZjc2lwCl91bnBpY2tsZV90eXBlCnEHWAwAAABQeVF0NS5RdENvcmVxCFgKAAAAUUJ5
dGVBcnJheXEJQ0IB2dDLAAMAAAAAA6oAAAJ4AAAFEwAAAv4AAAOrAAACpQAABRIAAAL9AAAAAAAA
AAAI0AAAA6sAAAKlAAAFEgAAAv1xCoVxC4dxDFJxDVgOAAAAc2V0X2JyZWFrcG9pbnRxDolYDgAA
AHdhcm11cF9zYW1wbGVzcQ9K/////3Uu
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWBcAAABkZWxheV9zdHJlYW1pbmdfcGFja2V0c3EBiVgIAAAAbWV0YWRhdGFxAn1xA1gT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUu
UXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAOqAAACagAABRMAAAMLAAADqwAA
ApcAAAUSAAADCgAAAAAAAAAACNAAAAOrAAAClwAABRIAAAMKcQiFcQmHcQpScQtYDgAAAHNldF9i
cmVha3BvaW50cQyJdS4=
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWBYAAABUZXN0XzA3LTIwMjMtMDMtMDIueGRmcQhYEwAAAGhhbmRsZV9jbG9j
a19yZXNldHNxCYhYEQAAAGhhbmRsZV9jbG9ja19zeW5jcQqIWBUAAABoYW5kbGVfaml0dGVyX3Jl
bW92YWxxC4hYDgAAAG1heF9tYXJrZXJfbGVucQxYDQAAACh1c2UgZGVmYXVsdClxDVgIAAAAbWV0
YWRhdGFxDn1xD1gSAAAAcmVvcmRlcl90aW1lc3RhbXBzcRCJWA4AAAByZXRhaW5fc3RyZWFtc3ER
aA1YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEmNzaXAKX3VucGlja2xlX3R5cGUKcRNYDAAAAFB5
UXQ1LlF0Q29yZXEUWAoAAABRQnl0ZUFycmF5cRVDQgHZ0MsAAwAAAAADqgAAAhkAAAUTAAADXAAA
A6sAAAJGAAAFEgAAA1sAAAAAAAAAAAjQAAADqwAAAkYAAAUSAAADW3EWhXEXh3EYUnEZWA4AAABz
ZXRfYnJlYWtwb2ludHEaiVgLAAAAdXNlX2NhY2hpbmdxG4lYDwAAAHVzZV9zdHJlYW1uYW1lc3Ec
iVgHAAAAdmVyYm9zZXEdiXUu
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWBAAAABkZXN0aW5hdGlvbl9ob3N0cQFYCQAAADEwLjAuMC4zMHECWBAAAABkZXN0aW5h
dGlvbl9wb3J0cQNNuCJYDwAAAG1lc3NhZ2VfYWRkcmVzc3EEWAUAAAAvZGF0YXEFWAgAAABtZXRh
ZGF0YXEGfXEHWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQhjc2lwCl91bnBpY2tsZV90eXBlCnEJ
WAwAAABQeVF0NS5RdENvcmVxClgKAAAAUUJ5dGVBcnJheXELQ0IB2dDLAAMAAAAAA6EAAAJIAAAF
HQAAAy4AAAOiAAACdQAABRwAAAMtAAAAAAAAAAAI0AAAA6IAAAJ1AAAFHAAAAy1xDIVxDYdxDlJx
D1gOAAAAc2V0X2JyZWFrcG9pbnRxEIl1Lg==
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node2",
            "data",
            "node3",
            "data"
        ],
        [
            "node3",
            "data",
            "node4",
            "data"
        ],
        [
            "node4",
            "data",
            "node5",
            "data"
        ],
        [
            "node1",
            "data",
            "node6",
            "data"
        ],
        [
            "node5",
            "data",
            "node7",
            "data"
        ],
        [
            "node6",
            "data",
            "node8",
            "data"
        ],
        [
            "node8",
            "data",
            "node2",
            "data"
        ],
        [
            "node9",
            "data",
            "node10",
            "data"
        ],
        [
            "node10",
            "data",
            "node11",
            "streaming_data"
        ],
        [
            "node11",
            "data",
            "node1",
            "data"
        ],
        [
            "node12",
            "data",
            "node11",
            "calib_data"
        ],
        [
            "node7",
            "data",
            "node13",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "AssignTargets",
            "module": "neuropype.nodes.machine_learning.AssignTargets",
            "params": {
                "also_legacy_output": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "is_categorical": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "mapping": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "left": 0,
                        "right": 1
                    }
                },
                "mapping_format": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "compat"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "b49a17d8-c29f-457c-8d60-38177fbe88bf"
        },
        "node10": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 300
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "f334662f-e9c8-452a-868d-4e00a4574036"
        },
        "node11": {
            "class": "InjectCalibrationData",
            "module": "neuropype.nodes.machine_learning.InjectCalibrationData",
            "params": {
                "delay_streaming_packets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "3d1b3a74-ff29-47a4-8ad9-9f3fc0c2652a"
        },
        "node12": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Test_07-2023-03-02.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_caching": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "2e59e739-de98-4f0a-bb81-8576111d3849"
        },
        "node13": {
            "class": "OSCOutput",
            "module": "neuropype.nodes.network.OSCOutput",
            "params": {
                "destination_host": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "10.0.0.30"
                },
                "destination_port": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 8888
                },
                "message_address": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "/data"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "47db5d5f-8cb6-4988-a5bf-840d0ffa5f96"
        },
        "node2": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "max_gap_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "online_epoching": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "sliding"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0.5,
                        3.5
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "ab15e38a-0308-4c99-8756-652b908e9dad"
        },
        "node3": {
            "class": "CommonSpatialPatterns",
            "module": "neuropype.nodes.neural.CommonSpatialPatterns",
            "params": {
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nof": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 2
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "257d6393-cd4f-471c-988a-c9d9f900e721"
        },
        "node4": {
            "class": "Variance",
            "module": "neuropype.nodes.statistics.Variance",
            "params": {
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "time"
                },
                "degrees_of_freedom": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "242f3894-14a6-4e10-b354-bf252110fd9f"
        },
        "node5": {
            "class": "Logarithm",
            "module": "neuropype.nodes.elementwise_math.Logarithm",
            "params": {
                "base": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "bd42a46b-8342-450a-b7c8-c1ca5059473a"
        },
        "node6": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "apply_time_selection_to_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": ":-6"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "c1857f49-c2aa-4d75-976e-47c0792dc687"
        },
        "node7": {
            "class": "LogisticRegression",
            "module": "neuropype.nodes.machine_learning.LogisticRegression",
            "params": {
                "alphas": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        1.0,
                        5,
                        10.0
                    ]
                },
                "bias_scaling": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "class_weights": {
                    "customized": true,
                    "type": "Port",
                    "value": "auto"
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "dual_formulation": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "feature_scaling": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "none"
                },
                "include_bias": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "l1_ratios": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "max_iter": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "multiclass": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "ovr"
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "num_jobs": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "random_seed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 12345
                },
                "regularizer": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "l2"
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "solver": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "lbfgs"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "07c44a21-942f-425e-90a6-e0630910562a"
        },
        "node8": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        6,
                        7,
                        30,
                        32
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "e151bea6-d740-4907-a4ee-6182747b7acd"
        },
        "node9": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_desc_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "omit_desc": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "prealloc_buffer": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_clocksync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_dejitter": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_monotonize": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_threadsafe": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='obci_eeg1'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "1aafd7dc-4182-4bb4-aadb-bf687638dd77"
        }
    },
    "version": 1.1
}</patch>
</scheme>
