suggestedStrategyComment = "OMEGA=115.746 KAPPA=128.047 PHI=259.585 STRATEGY=MERGED\n"
phi = 10.0
kap1 = 20.0
kap2 = 30.0
#mxv1StrategyResult = ""

mxv1InputCharacterisation = """
    <mxv1InputCharacterisation>
        <dataCollection>
            <diffractionPlan>
                <complexity>
                    <value>full</value>
                </complexity>
                <kappaStrategyOption>
                    <value>Cell</value>
                </kappaStrategyOption>
                <maxExposureTimePerDataCollection>
                    <value>1.000000e+03</value>
                </maxExposureTimePerDataCollection>
            </diffractionPlan>
            <subWedge>
                <experimentalCondition>
                    <beam>
                        <exposureTime>
                            <value>1.000000e-01</value>
                        </exposureTime>
                        <wavelength>
                            <value>9.792000e-01</value>
                        </wavelength>
                    </beam>
                    <detector>
                        <beamPositionX>
                            <value>1.575200e+02</value>
                        </beamPositionX>
                        <beamPositionY>
                            <value>1.566130e+02</value>
                        </beamPositionY>
                        <bin>
                            <value>2x2</value>
                        </bin>
                        <byteOrder>
                            <value>little_endian</value>
                        </byteOrder>
                        <dataType>
                            <value>unsigned_short</value>
                        </dataType>
                        <distance>
                            <value>3.408000e+02</value>
                        </distance>
                        <imageSaturation>
                            <value>65535</value>
                        </imageSaturation>
                        <name>
                            <value>ADSC Q315 bin 2x2</value>
                        </name>
                        <numberBytesInHeader>
                            <value>512</value>
                        </numberBytesInHeader>
                        <numberPixelX>
                            <value>3072</value>
                        </numberPixelX>
                        <numberPixelY>
                            <value>3072</value>
                        </numberPixelY>
                        <pixelSizeX>
                            <value>1.025880e-01</value>
                        </pixelSizeX>
                        <pixelSizeY>
                            <value>1.025880e-01</value>
                        </pixelSizeY>
                        <serialNumber>
                            <value>918</value>
                        </serialNumber>
                        <type>
                            <value>q315-2x</value>
                        </type>
                    </detector>
                    <goniostat>
                        <oscillationWidth>
                            <value>5.000000e-01</value>
                        </oscillationWidth>
                        <rotationAxis>
                            <value>phi</value>
                        </rotationAxis>
                        <rotationAxisEnd>
                            <value>9.100000e+01</value>
                        </rotationAxisEnd>
                        <rotationAxisStart>
                            <value>9.050000e+01</value>
                        </rotationAxisStart>
                    </goniostat>
                </experimentalCondition>
                <image>
                    <date>
                        <value>Wed Jun  1 14:58:51 2011</value>
                    </date>
                    <number>
                        <value>2</value>
                    </number>
                    <path>
                        <value>/data/id14eh4/inhouse/opid144/20110601/RAW_DATA/ref-edna_6_0002.img</value>
                    </path>
                </image>
            </subWedge>
            <subWedge>
                <experimentalCondition>
                    <beam>
                        <exposureTime>
                            <value>1.000000e-01</value>
                        </exposureTime>
                        <wavelength>
                            <value>9.792000e-01</value>
                        </wavelength>
                    </beam>
                    <detector>
                        <beamPositionX>
                            <value>1.575200e+02</value>
                        </beamPositionX>
                        <beamPositionY>
                            <value>1.566130e+02</value>
                        </beamPositionY>
                        <bin>
                            <value>2x2</value>
                        </bin>
                        <byteOrder>
                            <value>little_endian</value>
                        </byteOrder>
                        <dataType>
                            <value>unsigned_short</value>
                        </dataType>
                        <distance>
                            <value>3.408000e+02</value>
                        </distance>
                        <imageSaturation>
                            <value>65535</value>
                        </imageSaturation>
                        <name>
                            <value>ADSC Q315 bin 2x2</value>
                        </name>
                        <numberBytesInHeader>
                            <value>512</value>
                        </numberBytesInHeader>
                        <numberPixelX>
                            <value>3072</value>
                        </numberPixelX>
                        <numberPixelY>
                            <value>3072</value>
                        </numberPixelY>
                        <pixelSizeX>
                            <value>1.025880e-01</value>
                        </pixelSizeX>
                        <pixelSizeY>
                            <value>1.025880e-01</value>
                        </pixelSizeY>
                        <serialNumber>
                            <value>918</value>
                        </serialNumber>
                        <type>
                            <value>q315-2x</value>
                        </type>
                    </detector>
                    <goniostat>
                        <oscillationWidth>
                            <value>5.000000e-01</value>
                        </oscillationWidth>
                        <rotationAxis>
                            <value>phi</value>
                        </rotationAxis>
                        <rotationAxisEnd>
                            <value>5.000000e-01</value>
                        </rotationAxisEnd>
                        <rotationAxisStart>
                            <value>0.000000e+00</value>
                        </rotationAxisStart>
                    </goniostat>
                </experimentalCondition>
                <image>
                    <date>
                        <value>Wed Jun  1 14:58:49 2011</value>
                    </date>
                    <number>
                        <value>1</value>
                    </number>
                    <path>
                        <value>/data/id14eh4/inhouse/opid144/20110601/RAW_DATA/ref-edna_6_0001.img</value>
                    </path>
                </image>
            </subWedge>
        </dataCollection>
    </mxv1InputCharacterisation>
"""


mxv1ResultCharacterisation_Reference = """<mxv1ResultCharacterisation_Reference>
    <dataCollection>
        <diffractionPlan>
            <complexity>
                <value>full</value>
            </complexity>
            <kappaStrategyOption>
                <value>Cell</value>
            </kappaStrategyOption>
            <maxExposureTimePerDataCollection>
                <value>1.000000e+03</value>
            </maxExposureTimePerDataCollection>
        </diffractionPlan>
        <subWedge>
            <experimentalCondition>
                <beam>
                    <exposureTime>
                        <value>1.000000e+00</value>
                    </exposureTime>
                    <wavelength>
                        <value>9.340000e-01</value>
                    </wavelength>
                </beam>
                <detector>
                    <beamPositionX>
                        <value>1.024590e+02</value>
                    </beamPositionX>
                    <beamPositionY>
                        <value>1.047380e+02</value>
                    </beamPositionY>
                    <bin>
                        <value>2x2</value>
                    </bin>
                    <byteOrder>
                        <value>little_endian</value>
                    </byteOrder>
                    <dataType>
                        <value>unsigned_short</value>
                    </dataType>
                    <distance>
                        <value>1.984410e+02</value>
                    </distance>
                    <imageSaturation>
                        <value>65535</value>
                    </imageSaturation>
                    <name>
                        <value>ADSC Q210 bin 2x2</value>
                    </name>
                    <numberBytesInHeader>
                        <value>512</value>
                    </numberBytesInHeader>
                    <numberPixelX>
                        <value>2048</value>
                    </numberPixelX>
                    <numberPixelY>
                        <value>2048</value>
                    </numberPixelY>
                    <pixelSizeX>
                        <value>1.024000e-01</value>
                    </pixelSizeX>
                    <pixelSizeY>
                        <value>1.024000e-01</value>
                    </pixelSizeY>
                    <serialNumber>
                        <value>444</value>
                    </serialNumber>
                    <twoTheta>
                        <value>0.000000e+00</value>
                    </twoTheta>
                    <type>
                        <value>q210-2x</value>
                    </type>
                </detector>
                <goniostat>
                    <oscillationWidth>
                        <value>1.000000e+00</value>
                    </oscillationWidth>
                    <rotationAxis>
                        <value>phi</value>
                    </rotationAxis>
                    <rotationAxisEnd>
                        <value>9.100000e+01</value>
                    </rotationAxisEnd>
                    <rotationAxisStart>
                        <value>9.000000e+01</value>
                    </rotationAxisStart>
                </goniostat>
            </experimentalCondition>
            <image>
                <date>
                    <value>Mon Mar 20 12:38:28 2006</value>
                </date>
                <number>
                    <value>2</value>
                </number>
                <path>
                    <value>/opt/pxsoft/DNA/TestCase/RAW_DATA/ref-testscale_1_0002.img</value>
                </path>
            </image>
        </subWedge>
        <subWedge>
            <experimentalCondition>
                <beam>
                    <exposureTime>
                        <value>1.000000e+00</value>
                    </exposureTime>
                    <wavelength>
                        <value>9.340000e-01</value>
                    </wavelength>
                </beam>
                <detector>
                    <beamPositionX>
                        <value>1.024590e+02</value>
                    </beamPositionX>
                    <beamPositionY>
                        <value>1.047380e+02</value>
                    </beamPositionY>
                    <bin>
                        <value>2x2</value>
                    </bin>
                    <byteOrder>
                        <value>little_endian</value>
                    </byteOrder>
                    <dataType>
                        <value>unsigned_short</value>
                    </dataType>
                    <distance>
                        <value>1.984410e+02</value>
                    </distance>
                    <imageSaturation>
                        <value>65535</value>
                    </imageSaturation>
                    <name>
                        <value>ADSC Q210 bin 2x2</value>
                    </name>
                    <numberBytesInHeader>
                        <value>512</value>
                    </numberBytesInHeader>
                    <numberPixelX>
                        <value>2048</value>
                    </numberPixelX>
                    <numberPixelY>
                        <value>2048</value>
                    </numberPixelY>
                    <pixelSizeX>
                        <value>1.024000e-01</value>
                    </pixelSizeX>
                    <pixelSizeY>
                        <value>1.024000e-01</value>
                    </pixelSizeY>
                    <serialNumber>
                        <value>444</value>
                    </serialNumber>
                    <twoTheta>
                        <value>0.000000e+00</value>
                    </twoTheta>
                    <type>
                        <value>q210-2x</value>
                    </type>
                </detector>
                <goniostat>
                    <oscillationWidth>
                        <value>1.000000e+00</value>
                    </oscillationWidth>
                    <rotationAxis>
                        <value>phi</value>
                    </rotationAxis>
                    <rotationAxisEnd>
                        <value>1.000000e+00</value>
                    </rotationAxisEnd>
                    <rotationAxisStart>
                        <value>0.000000e+00</value>
                    </rotationAxisStart>
                </goniostat>
            </experimentalCondition>
            <image>
                <date>
                    <value>Mon Mar 20 12:38:23 2006</value>
                </date>
                <number>
                    <value>1</value>
                </number>
                <path>
                    <value>/opt/pxsoft/DNA/TestCase/RAW_DATA/ref-testscale_1_0001.img</value>
                </path>
            </image>
        </subWedge>
    </dataCollection>
    <imageQualityIndicators>
        <binPopCutOffMethod2Res>
            <value>2.000000e+01</value>
        </binPopCutOffMethod2Res>
        <goodBraggCandidates>
            <value>1224</value>
        </goodBraggCandidates>
        <iceRings>
            <value>0</value>
        </iceRings>
        <image>
            <date>
                <value>Mon Mar 20 12:38:28 2006</value>
            </date>
            <number>
                <value>2</value>
            </number>
            <path>
                <value>/opt/pxsoft/DNA/TestCase/RAW_DATA/ref-testscale_1_0002.img</value>
            </path>
        </image>
        <inResTotal>
            <value>1431</value>
        </inResTotal>
        <inResolutionOvrlSpots>
            <value>1</value>
        </inResolutionOvrlSpots>
        <maxUnitCell>
            <value>2.082000e+02</value>
        </maxUnitCell>
        <method1Res>
            <value>1.910000e+00</value>
        </method1Res>
        <method2Res>
            <value>1.820000e+00</value>
        </method2Res>
        <pctSaturationTop50Peaks>
            <value>2.051000e+01</value>
        </pctSaturationTop50Peaks>
        <saturationRangeAverage>
            <value>1.500000e+00</value>
        </saturationRangeAverage>
        <saturationRangeMax>
            <value>9.990000e+01</value>
        </saturationRangeMax>
        <saturationRangeMin>
            <value>0.000000e+00</value>
        </saturationRangeMin>
        <signalRangeAverage>
            <value>9.993100e+03</value>
        </signalRangeAverage>
        <signalRangeMax>
            <value>4.176627e+05</value>
        </signalRangeMax>
        <signalRangeMin>
            <value>2.107000e+02</value>
        </signalRangeMin>
        <spotTotal>
            <value>1524</value>
        </spotTotal>
        <totalIntegratedSignal>
            <value>1.089628e+07</value>
        </totalIntegratedSignal>
    </imageQualityIndicators>
    <imageQualityIndicators>
        <binPopCutOffMethod2Res>
            <value>2.000000e+01</value>
        </binPopCutOffMethod2Res>
        <goodBraggCandidates>
            <value>1042</value>
        </goodBraggCandidates>
        <iceRings>
            <value>0</value>
        </iceRings>
        <image>
            <date>
                <value>Mon Mar 20 12:38:23 2006</value>
            </date>
            <number>
                <value>1</value>
            </number>
            <path>
                <value>/opt/pxsoft/DNA/TestCase/RAW_DATA/ref-testscale_1_0001.img</value>
            </path>
        </image>
        <inResTotal>
            <value>1332</value>
        </inResTotal>
        <inResolutionOvrlSpots>
            <value>1</value>
        </inResolutionOvrlSpots>
        <maxUnitCell>
            <value>2.064000e+02</value>
        </maxUnitCell>
        <method1Res>
            <value>1.890000e+00</value>
        </method1Res>
        <method2Res>
            <value>1.870000e+00</value>
        </method2Res>
        <pctSaturationTop50Peaks>
            <value>1.934000e+01</value>
        </pctSaturationTop50Peaks>
        <saturationRangeAverage>
            <value>1.500000e+00</value>
        </saturationRangeAverage>
        <saturationRangeMax>
            <value>9.980000e+01</value>
        </saturationRangeMax>
        <saturationRangeMin>
            <value>0.000000e+00</value>
        </saturationRangeMin>
        <signalRangeAverage>
            <value>1.096120e+04</value>
        </signalRangeAverage>
        <signalRangeMax>
            <value>4.297496e+05</value>
        </signalRangeMax>
        <signalRangeMin>
            <value>2.613000e+02</value>
        </signalRangeMin>
        <spotTotal>
            <value>1432</value>
        </spotTotal>
        <totalIntegratedSignal>
            <value>1.041617e+07</value>
        </totalIntegratedSignal>
    </imageQualityIndicators>
    <indexingResult>
        <image>
            <date>
                <value>Mon Mar 20 12:38:28 2006</value>
            </date>
            <number>
                <value>2</value>
            </number>
            <path>
                <value>/opt/pxsoft/DNA/TestCase/RAW_DATA/ref-testscale_1_0002.img</value>
            </path>
        </image>
        <image>
            <date>
                <value>Mon Mar 20 12:38:23 2006</value>
            </date>
            <number>
                <value>1</value>
            </number>
            <path>
                <value>/opt/pxsoft/DNA/TestCase/RAW_DATA/ref-testscale_1_0001.img</value>
            </path>
        </image>
        <predictionResult>
            <predictionImage>
                <number>
                    <value>2</value>
                </number>
                <path>
                    <value>/users/svensson/dawb_workspace/workflows-id14eh4/edna-working-dir/ControlCharForReorientationv2_0-00000083/MXv1Characterisation/GeneratePrediction/MOSFLMGeneratePredictionv10-01/ref-testscale_1_0002_pred.jpg</value>
                </path>
            </predictionImage>
            <predictionImage>
                <number>
                    <value>1</value>
                </number>
                <path>
                    <value>/users/svensson/dawb_workspace/workflows-id14eh4/edna-working-dir/ControlCharForReorientationv2_0-00000083/MXv1Characterisation/GeneratePrediction/MOSFLMGeneratePredictionv10-02/ref-testscale_1_0001_pred.jpg</value>
                </path>
            </predictionImage>
        </predictionResult>
        <selectedSolution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.000000e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.000000e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.000000e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.480450e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.907400e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698280e+01</value>
                    </length_c>
                </cell>
                <mosaicity>
                    <value>5.850000e-01</value>
                </mosaicity>
                <spaceGroup>
                    <ITNumber>
                        <value>16</value>
                    </ITNumber>
                    <name>
                        <value>P222</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>5</value>
            </number>
            <penalty>
                <value>0.000000e+00</value>
            </penalty>
            <experimentalConditionRefined>
                <beam>
                    <exposureTime>
                        <value>1.000000e+00</value>
                    </exposureTime>
                    <wavelength>
                        <value>9.340000e-01</value>
                    </wavelength>
                </beam>
                <detector>
                    <beamPositionX>
                        <value>1.024770e+02</value>
                    </beamPositionX>
                    <beamPositionY>
                        <value>1.048865e+02</value>
                    </beamPositionY>
                    <bin>
                        <value>2x2</value>
                    </bin>
                    <byteOrder>
                        <value>little_endian</value>
                    </byteOrder>
                    <dataType>
                        <value>unsigned_short</value>
                    </dataType>
                    <distance>
                        <value>1.984410e+02</value>
                    </distance>
                    <imageSaturation>
                        <value>65535</value>
                    </imageSaturation>
                    <name>
                        <value>ADSC Q210 bin 2x2</value>
                    </name>
                    <numberBytesInHeader>
                        <value>512</value>
                    </numberBytesInHeader>
                    <numberPixelX>
                        <value>2048</value>
                    </numberPixelX>
                    <numberPixelY>
                        <value>2048</value>
                    </numberPixelY>
                    <pixelSizeX>
                        <value>1.024000e-01</value>
                    </pixelSizeX>
                    <pixelSizeY>
                        <value>1.024000e-01</value>
                    </pixelSizeY>
                    <serialNumber>
                        <value>444</value>
                    </serialNumber>
                    <twoTheta>
                        <value>0.000000e+00</value>
                    </twoTheta>
                    <type>
                        <value>q210-2x</value>
                    </type>
                </detector>
                <goniostat>
                    <oscillationWidth>
                        <value>1.000000e+00</value>
                    </oscillationWidth>
                    <rotationAxis>
                        <value>phi</value>
                    </rotationAxis>
                    <rotationAxisEnd>
                        <value>9.100000e+01</value>
                    </rotationAxisEnd>
                    <rotationAxisStart>
                        <value>9.000000e+01</value>
                    </rotationAxisStart>
                </goniostat>
            </experimentalConditionRefined>
            <orientation>
                <matrixA>
                    <m11>-8.264460e-03</m11>
                    <m12>8.851170e-03</m12>
                    <m13>9.368760e-03</m13>
                    <m21>1.266330e-03</m21>
                    <m22>1.251994e-02</m22>
                    <m23>-8.452180e-03</m23>
                    <m31>-1.485053e-02</m31>
                    <m32>-3.858160e-03</m32>
                    <m33>-5.934530e-03</m33>
                </matrixA>
                <matrixU>
                    <m11>-4.849355e-01</m11>
                    <m12>5.598223e-01</m12>
                    <m13>6.718904e-01</m13>
                    <m21>7.430480e-02</m21>
                    <m22>7.918661e-01</m22>
                    <m23>-6.061574e-01</m23>
                    <m31>-8.713877e-01</m31>
                    <m32>-2.440224e-01</m32>
                    <m33>-4.256014e-01</m33>
                </matrixU>
            </orientation>
            <statistics>
                <beamPositionShiftX>
                    <value>-1.802100e-02</value>
                </beamPositionShiftX>
                <beamPositionShiftY>
                    <value>-1.484600e-01</value>
                </beamPositionShiftY>
                <spotDeviationAngular>
                    <value>4.361550e-01</value>
                </spotDeviationAngular>
                <spotDeviationPositional>
                    <value>1.496080e-01</value>
                </spotDeviationPositional>
                <spotsTotal>
                    <value>1434</value>
                </spotsTotal>
                <spotsUsed>
                    <value>1287</value>
                </spotsUsed>
            </statistics>
        </selectedSolution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001893e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>6.805720e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>1.009895e+02</value>
                    </angle_gamma>
                    <length_a>
                        <value>1.463975e+02</value>
                    </length_a>
                    <length_b>
                        <value>8.931725e+01</value>
                    </length_b>
                    <length_c>
                        <value>5.481434e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>hR</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>44</value>
            </number>
            <penalty>
                <value>9.990000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>1.113587e+02</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>1.005142e+02</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>1.169248e+02</value>
                    </angle_gamma>
                    <length_a>
                        <value>1.048114e+02</value>
                    </length_a>
                    <length_b>
                        <value>1.047805e+02</value>
                    </length_b>
                    <length_c>
                        <value>1.047389e+02</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>cF</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>43</value>
            </number>
            <penalty>
                <value>7.780000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>6.103973e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>5.454230e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>6.451337e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.652050e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.056377e+01</value>
                    </length_b>
                    <length_c>
                        <value>8.930070e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>cI</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>42</value>
            </number>
            <penalty>
                <value>7.770000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>5.849593e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>8.998107e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.611723e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.931724e+01</value>
                    </length_a>
                    <length_b>
                        <value>1.047388e+02</value>
                    </length_b>
                    <length_c>
                        <value>5.481434e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>tI</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>41</value>
            </number>
            <penalty>
                <value>7.420000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>1.121866e+02</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>1.371263e+02</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>5.900963e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.056374e+01</value>
                    </length_a>
                    <length_b>
                        <value>1.562835e+02</value>
                    </length_b>
                    <length_c>
                        <value>5.906597e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mI</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>40</value>
            </number>
            <penalty>
                <value>7.390000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.162820e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>1.046281e+02</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>1.328482e+02</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.056377e+01</value>
                    </length_b>
                    <length_c>
                        <value>2.164904e+02</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>hR</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>39</value>
            </number>
            <penalty>
                <value>7.040000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>8.086137e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>1.122105e+02</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>1.148708e+02</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>1.302075e+02</value>
                    </length_b>
                    <length_c>
                        <value>1.447121e+02</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oF</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>38</value>
            </number>
            <penalty>
                <value>6.680000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>6.451337e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>6.103973e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>5.454230e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.930070e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.652049e+01</value>
                    </length_b>
                    <length_c>
                        <value>8.056377e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>tI</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>37</value>
            </number>
            <penalty>
                <value>5.910000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>6.103973e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>5.454230e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>6.451337e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.652050e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.056377e+01</value>
                    </length_b>
                    <length_c>
                        <value>8.930070e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>tI</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>36</value>
            </number>
            <penalty>
                <value>5.910000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>5.454230e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>6.103973e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>6.451337e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.056377e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.652051e+01</value>
                    </length_b>
                    <length_c>
                        <value>8.930070e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oI</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>35</value>
            </number>
            <penalty>
                <value>5.900000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>8.388277e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>5.849593e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.001893e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.931724e+01</value>
                    </length_b>
                    <length_c>
                        <value>1.047388e+02</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oI</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>34</value>
            </number>
            <penalty>
                <value>5.190000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.222399e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>1.209904e+02</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>8.572379e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.056376e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.059953e+01</value>
                    </length_b>
                    <length_c>
                        <value>1.562835e+02</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oF</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>33</value>
            </number>
            <penalty>
                <value>5.170000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>6.451337e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>1.155142e+02</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>8.572380e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.059953e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.056376e+01</value>
                    </length_b>
                    <length_c>
                        <value>8.652051e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>32</value>
            </number>
            <penalty>
                <value>5.160000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>6.781336e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>6.952161e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.002551e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481433e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.906598e+01</value>
                    </length_b>
                    <length_c>
                        <value>1.562835e+02</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>tI</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>31</value>
            </number>
            <penalty>
                <value>4.810000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>1.121866e+02</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>1.104784e+02</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.002551e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481433e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.906598e+01</value>
                    </length_b>
                    <length_c>
                        <value>1.562835e+02</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oI</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>30</value>
            </number>
            <penalty>
                <value>4.810000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001893e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>1.268872e+02</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>6.512925e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>1.302075e+02</value>
                    </length_a>
                    <length_b>
                        <value>5.481434e+01</value>
                    </length_b>
                    <length_c>
                        <value>8.931724e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>29</value>
            </number>
            <penalty>
                <value>4.450000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.004773e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.002551e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.001070e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.906598e+01</value>
                    </length_a>
                    <length_b>
                        <value>6.698733e+01</value>
                    </length_b>
                    <length_c>
                        <value>5.481433e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>hP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>28</value>
            </number>
            <penalty>
                <value>3.330000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001070e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004773e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.002551e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.906598e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698733e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>hP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>27</value>
            </number>
            <penalty>
                <value>2.590000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001958e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.002551e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>6.778947e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481433e+01</value>
                    </length_a>
                    <length_b>
                        <value>1.447121e+02</value>
                    </length_b>
                    <length_c>
                        <value>5.906598e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>26</value>
            </number>
            <penalty>
                <value>2.580000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>8.998043e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.002551e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>1.122105e+02</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481433e+01</value>
                    </length_a>
                    <length_b>
                        <value>1.447121e+02</value>
                    </length_b>
                    <length_c>
                        <value>5.906598e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>25</value>
            </number>
            <penalty>
                <value>2.580000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.002551e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.001958e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>6.778947e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>1.447121e+02</value>
                    </length_a>
                    <length_b>
                        <value>5.481433e+01</value>
                    </length_b>
                    <length_c>
                        <value>5.906598e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>24</value>
            </number>
            <penalty>
                <value>2.580000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001958e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.002551e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>6.778947e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481433e+01</value>
                    </length_a>
                    <length_b>
                        <value>1.447121e+02</value>
                    </length_b>
                    <length_c>
                        <value>5.906598e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>23</value>
            </number>
            <penalty>
                <value>2.230000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.002981e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004773e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>6.512926e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>1.302075e+02</value>
                    </length_b>
                    <length_c>
                        <value>6.698734e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>22</value>
            </number>
            <penalty>
                <value>2.230000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>8.997020e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004773e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>1.148708e+02</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>1.302075e+02</value>
                    </length_b>
                    <length_c>
                        <value>6.698734e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>21</value>
            </number>
            <penalty>
                <value>2.230000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.004773e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.002981e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>6.512926e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>1.302075e+02</value>
                    </length_a>
                    <length_b>
                        <value>5.481433e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698733e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>20</value>
            </number>
            <penalty>
                <value>2.230000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>8.998043e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.002551e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>1.122105e+02</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481433e+01</value>
                    </length_a>
                    <length_b>
                        <value>1.447121e+02</value>
                    </length_b>
                    <length_c>
                        <value>5.906598e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>19</value>
            </number>
            <penalty>
                <value>2.220000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.002551e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.001958e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>6.778947e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>1.447121e+02</value>
                    </length_a>
                    <length_b>
                        <value>5.481433e+01</value>
                    </length_b>
                    <length_c>
                        <value>5.906598e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>18</value>
            </number>
            <penalty>
                <value>2.220000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.941354e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>8.669627e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>1.155341e+02</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.059952e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.659118e+01</value>
                    </length_b>
                    <length_c>
                        <value>1.047388e+02</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>hR</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>17</value>
            </number>
            <penalty>
                <value>1.100000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.942419e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>8.673009e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>1.155142e+02</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.059952e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.652050e+01</value>
                    </length_b>
                    <length_c>
                        <value>1.048113e+02</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>hR</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>16</value>
            </number>
            <penalty>
                <value>1.100000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001070e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004773e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.002551e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.906598e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698733e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>cP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>15</value>
            </number>
            <penalty>
                <value>1.100000e+02</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>8.998107e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.005268e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.719164e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.930071e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.931725e+01</value>
                    </length_b>
                    <length_c>
                        <value>5.481435e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>14</value>
            </number>
            <penalty>
                <value>7.400000e+01</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.004773e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.002551e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.001070e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.906598e+01</value>
                    </length_a>
                    <length_b>
                        <value>6.698733e+01</value>
                    </length_b>
                    <length_c>
                        <value>5.481433e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>tP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>13</value>
            </number>
            <penalty>
                <value>7.400000e+01</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001893e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.005268e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>8.280837e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.930071e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.931725e+01</value>
                    </length_b>
                    <length_c>
                        <value>5.481435e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>12</value>
            </number>
            <penalty>
                <value>7.400000e+01</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001893e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.005268e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>8.280837e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.930071e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.931725e+01</value>
                    </length_b>
                    <length_c>
                        <value>5.481435e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>11</value>
            </number>
            <penalty>
                <value>7.400000e+01</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.002462e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004033e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.427621e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.056376e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.059953e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698734e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>10</value>
            </number>
            <penalty>
                <value>3.600000e+01</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001070e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004773e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.002551e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.906598e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698733e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>tP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>9</value>
            </number>
            <penalty>
                <value>3.600000e+01</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>8.997539e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004033e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>8.572379e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.056376e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.059953e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698734e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>8</value>
            </number>
            <penalty>
                <value>3.600000e+01</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>8.997539e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004033e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>8.572379e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>8.056376e+01</value>
                    </length_a>
                    <length_b>
                        <value>8.059953e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698734e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mC</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>7</value>
            </number>
            <penalty>
                <value>3.600000e+01</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001070e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>8.995227e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>8.997449e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.906598e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698733e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>aP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>6</value>
            </number>
            <penalty>
                <value>0.000000e+00</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001070e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004773e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.002551e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.906598e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698733e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>oP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>5</value>
            </number>
            <penalty>
                <value>0.000000e+00</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001070e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004773e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.002551e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.906598e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698733e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>4</value>
            </number>
            <penalty>
                <value>0.000000e+00</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001070e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.002551e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.004773e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>6.698733e+01</value>
                    </length_b>
                    <length_c>
                        <value>5.906598e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>3</value>
            </number>
            <penalty>
                <value>0.000000e+00</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.004773e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.001070e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.002551e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.906598e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.481433e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698733e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>mP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>2</value>
            </number>
            <penalty>
                <value>0.000000e+00</value>
            </penalty>
        </solution>
        <solution>
            <crystal>
                <cell>
                    <angle_alpha>
                        <value>9.001070e+01</value>
                    </angle_alpha>
                    <angle_beta>
                        <value>9.004773e+01</value>
                    </angle_beta>
                    <angle_gamma>
                        <value>9.002551e+01</value>
                    </angle_gamma>
                    <length_a>
                        <value>5.481434e+01</value>
                    </length_a>
                    <length_b>
                        <value>5.906598e+01</value>
                    </length_b>
                    <length_c>
                        <value>6.698733e+01</value>
                    </length_c>
                </cell>
                <spaceGroup>
                    <name>
                        <value>aP</value>
                    </name>
                </spaceGroup>
            </crystal>
            <number>
                <value>1</value>
            </number>
            <penalty>
                <value>0.000000e+00</value>
            </penalty>
        </solution>
    </indexingResult>
    <integrationResult>
        <integrationSubWedgeResult>
            <bestfileDat>
                <value>   90.5036      60.75       3.38
75.4210      59.75       3.34
64.6479      58.75       3.30
56.5683      64.50       3.52
50.2843      67.50       3.62
45.2572      70.75       3.73
41.1443      66.75       3.59
37.7170      72.50       3.79
34.8171      66.50       3.57
32.3315      68.00       3.64
30.1775      73.50       3.82
28.2928      68.50       3.65
26.6299      72.00       3.77
25.1519      70.25       3.72
23.8295      70.50       3.72
22.6394      67.75       3.63
21.5628      72.25       3.78
20.5841      70.50       3.72
19.6905      71.00       3.74
18.8715      69.25       3.68
18.1181      71.75       3.77
17.4226      69.00       3.67
16.7788      65.00       3.53
16.1809      71.50       3.76
15.6244      68.25       3.65
15.1050      70.00       3.70
14.6192      70.25       3.72
14.1637      66.00       3.56
13.7359      71.50       3.76
13.3334      64.50       3.50
12.9538      64.00       3.50
12.5954      70.50       3.72
12.2564      68.25       3.65
11.9353      58.50       3.28
11.6307      66.75       3.60
11.3414      66.00       3.57
11.0662      67.25       3.61
10.8041      66.00       3.57
10.5543      68.75       3.67
10.3158      67.50       3.62
10.0880      62.75       3.45
9.8701      64.00       3.50
9.6615      65.75       3.56
9.4617      66.00       3.57
9.2700      62.50       3.45
9.0860      65.25       3.54
8.9093      64.25       3.51
8.7394      62.25       3.43
8.5759      61.25       3.40
8.4185      58.00       3.28
8.2669      62.00       3.43
8.1207      63.00       3.46
7.9796      62.50       3.45
7.8435      62.25       3.43
7.7120      61.25       3.40
7.5849      56.50       3.22
7.4619      54.25       3.11
7.3430      64.75       3.53
7.2279      57.25       3.25
7.1164      60.25       3.36
7.0083      59.50       3.33
6.9035      57.00       3.24
6.8019      55.25       3.16
6.7033      58.00       3.27
6.6076      60.25       3.36
6.5146      62.50       3.45
6.4243      59.75       3.34
6.3365      59.50       3.33
6.2511      56.75       3.22
6.1680      59.00       3.32
6.0872      59.25       3.32
6.0085      61.75       3.42
5.9319      59.75       3.34
5.8573      63.75       3.49
5.7846      59.00       3.31
5.7137      60.50       3.37
5.6445      61.00       3.39
5.5771      62.75       3.45
5.5113      55.75       3.19
5.4471      54.00       3.10
5.3845      60.75       3.38
5.3233      63.25       3.47
5.2635      64.75       3.53
5.2051      60.25       3.36
5.1480      60.25       3.36
5.0922      63.75       3.49
5.0377      64.00       3.50
4.9843      67.25       3.61
4.9322      65.00       3.54
4.8811      62.75       3.45
4.8311      64.75       3.53
4.7822      66.00       3.57
4.7343      68.50       3.66
4.6874      68.00       3.64
4.6415      62.25       3.43
4.5965      67.00       3.60
4.5524      70.00       3.70
4.5091      75.00       3.87
4.4668      74.75       3.86
4.4252      73.25       3.81
4.3845      79.75       4.02
4.3445      76.50       3.92
4.3053      78.75       3.99
4.2669      77.00       3.94
4.2291      76.75       3.92
4.1921      81.25       4.07
4.1557      83.00       4.12
4.1200      84.50       4.17
4.0849      85.50       4.20
4.0505      86.00       4.21
4.0167      77.00       3.92
3.9835      87.75       4.26
3.9508      94.50       4.46
3.9187      91.00       4.36
3.8872      92.50       4.40
3.8562      92.25       4.39
3.8257      95.00       4.47
3.7957      95.50       4.49
3.7663      91.75       4.37
3.7373      96.50       4.51
3.7088      97.00       4.53
3.6807      97.50       4.54
3.6532      92.50       4.40
3.6260      89.75       4.32
3.5993      95.50       4.48
3.5730     102.25       4.67
3.5471     101.75       4.66
3.5216      92.00       4.38
3.4965      98.75       4.58
3.4718     103.25       4.70
3.4475      98.00       4.55
3.4235      98.25       4.56
3.3999     101.25       4.64
3.3766      98.00       4.56
3.3537      94.50       4.46
3.3312      91.75       4.38
3.3089      91.00       4.36
3.2870      91.25       4.37
3.2654      91.50       4.37
3.2441      86.50       4.23
3.2231      85.00       4.18
3.2024      86.50       4.23
3.1820      87.50       4.26
3.1618      83.00       4.12
3.1420      78.25       3.97
3.1224      79.00       3.99
3.1031      73.75       3.83
3.0841      70.50       3.72
3.0653      72.00       3.77
3.0468      73.50       3.82
3.0285      68.75       3.66
3.0104      69.50       3.69
2.9926      71.00       3.74
2.9750      70.75       3.73
2.9577      67.25       3.61
2.9406      59.75       3.34
2.9237      63.00       3.46
2.9070      63.75       3.49
2.8905      60.50       3.37
2.8742      56.25       3.21
2.8582      57.75       3.27
2.8423      59.75       3.34
2.8267      55.25       3.17
2.8112      59.50       3.33
2.7959      56.50       3.22
2.7808      53.50       3.10
2.7659      53.00       3.08
2.7512      55.50       3.18
2.7366      54.75       3.15
2.7222      49.50       2.94
2.7080      54.00       3.12
2.6940      54.75       3.15
2.6801      50.50       2.98
2.6664      45.75       2.74
2.6529      53.50       3.10
2.6395      53.50       3.10
2.6262      50.50       2.98
2.6132      51.00       3.00
2.6002      48.00       2.87
2.5874      47.00       2.82
2.5748      51.50       3.02
2.5623      49.00       2.91
2.5499      44.25       2.69
2.5377      46.50       2.81
2.5256      51.75       3.03
2.5136      47.50       2.85
2.5018      48.75       2.90
2.4901      51.00       3.00
2.4785      50.00       2.96
2.4671      41.25       2.56
2.4558      46.00       2.78
2.4446      42.00       2.57
2.4335      45.25       2.75
2.4225      48.75       2.90
2.4117      44.25       2.68
2.4010      43.50       2.67
2.3903      44.75       2.73
2.3798      50.00       2.96
2.3694      43.75       2.67
2.3591      48.00       2.86
2.3489      51.75       3.03
2.3389      45.25       2.75
2.3289      49.25       2.93
2.3190      46.75       2.81
2.3092      49.75       2.94
2.2995      44.00       2.69
2.2900      51.00       3.00
2.2805      48.25       2.87
2.2711      44.50       2.70
2.2618      43.75       2.67
2.2526      46.50       2.81
2.2434      52.25       3.05
2.2344      52.50       3.06
2.2255      46.25       2.77
2.2166      51.75       3.03
2.2078      52.00       3.04
2.1992      49.50       2.93
2.1905      51.00       3.00
2.1820      50.75       2.99
2.1736      50.75       2.99
2.1652      52.00       3.04
2.1569      52.50       3.06
2.1487      47.75       2.86
2.1406      50.75       2.99
2.1326      50.50       2.98
2.1246      47.25       2.83
2.1167      49.75       2.94
2.1088      51.50       3.02
2.1011      48.00       2.87
2.0934      50.75       2.99
2.0858      46.50       2.79
2.0782      42.75       2.62
2.0707      51.00       3.00
2.0633      50.50       2.97
2.0560      47.75       2.86
2.0487      48.75       2.90
2.0415      46.50       2.81
2.0343      45.00       2.73
2.0272      43.75       2.67
2.0202      43.00       2.64
2.0132      46.00       2.78
2.0063      43.00       2.64
1.9995      37.50       2.36
1.9927      41.50       2.57
1.9859      42.50       2.70
1.9793      20.00       1.25
</value>
            </bestfileDat>
            <bestfileHKL>
                <value>  -6  -12  -40     658.25      87.10
-6  -12  -39     566.71     102.32
-5  -12  -39     532.84      80.20
-4  -12  -39    1647.91     105.50
-5  -12  -38    1353.87     113.26
-4  -12  -38    1994.87     128.97
-3  -12  -38     952.77     132.72
-5  -12  -37     496.90      84.17
-4  -12  -37     204.16      70.56
-3  -12  -37    2066.08     103.30
-5  -12  -36    -188.41     128.77
-4  -12  -36    4337.20     228.23
-3  -12  -36     898.20      61.28
-2  -12  -36    6280.17     245.35
-4  -12  -35     430.68      64.55
-3  -12  -35     742.20      77.01
-2  -12  -35     828.10      64.18
-1  -12  -35    1730.53     111.62
-3  -12  -34    1010.14      71.26
-2  -12  -34    7603.68     159.20
-1  -12  -34    1307.85      74.37
0  -12  -34    2869.16     134.05
-2  -12  -33     635.41      61.60
-1  -12  -33    1827.01      80.86
0  -12  -33     607.50      58.49
1  -12  -33    2098.43     102.39
2  -12  -33     902.56      86.78
3  -12  -33    2005.70     124.80
4  -12  -33    4123.68     188.81
5  -12  -33    2309.10     126.61
-1  -12  -32     483.78      65.43
0  -12  -32     680.52      75.47
1  -12  -32     978.97      73.86
2  -12  -32     367.65      70.43
3  -12  -32     304.64      58.95
4  -12  -32    7585.17     304.30
5  -12  -32    8788.62     345.00
6  -12  -32    1889.44      82.35
7  -12  -32    3899.63     108.67
0  -12  -31      91.03      91.71
1  -12  -31     213.56      64.77
2  -12  -31    2788.99     127.22
3  -12  -31    5481.38     116.54
4  -12  -31    6559.98     133.32
5  -12  -31    1346.20      81.15
6  -12  -31     709.89      80.50
7  -12  -31    6064.75     223.97
8  -12  -31    1279.49      86.61
3  -12  -30     489.18     102.21
4  -12  -30    2062.06     128.72
5  -12  -30    1452.18     116.86
6  -12  -30    2377.71     148.56
-9  -11  -41    5032.91     318.11
-9  -11  -40     359.47     107.76
-10  -11  -39     -32.59      70.87
-9  -11  -39    1370.54     108.64
-10  -11  -38     670.44      96.69
-9  -11  -38    1030.83      85.33
-9  -11  -37    1182.36      91.56
-9  -11  -36     567.37      68.59
-8  -11  -36     278.19     101.47
-9  -11  -35      74.90      87.78
-8  -11  -35    4115.28     215.44
-8  -11  -34    2541.52      93.04
-7  -11  -34    2979.74     190.80
-8  -11  -33    1083.69     100.32
-7  -11  -33    1606.52      98.70
-7  -11  -32    1333.78      91.21
-6  -11  -32    4007.33     166.43
-6  -11  -31    3440.08      95.07
-5  -11  -31   38467.32    1438.80
-6  -11  -30    7937.27     290.94
-5  -11  -30    9571.32     148.89
-4  -11  -30    2093.04     123.55
-5  -11  -29    2347.51     110.71
-4  -11  -29    1857.46      82.55
-3  -11  -29     950.41      76.49
11  -11  -29    1257.24      88.82
12  -11  -29    5655.33     124.93
-4  -11  -28    1685.84     108.01
-3  -11  -28    1744.52      75.24
-2  -11  -28   12552.49     436.31
9  -11  -28   54536.85    1911.10
10  -11  -28    2920.12     130.57
11  -11  -28     221.01      72.61
12  -11  -28    4867.56     192.17
-2  -11  -27    4714.78     179.70
-1  -11  -27    9229.34     133.81
0  -11  -27   14897.00     516.05
1  -11  -27   11564.00     434.95
6  -11  -27   13731.53     487.46
7  -11  -27    9622.46     346.15
8  -11  -27    3441.06     136.36
9  -11  -27    2041.57      82.73
10  -11  -27   11414.80     168.83
11  -11  -27    1525.68     101.52
0  -11  -26    2276.51      97.28
1  -11  -26    7454.64     114.75
2  -11  -26   12795.46     163.33
3  -11  -26    5035.62      95.75
4  -11  -26    2913.77      83.74
5  -11  -26   16177.93     191.97
6  -11  -26    2376.43      85.65
7  -11  -26     984.07      75.91
8  -11  -26   12724.63     441.16
9  -11  -26    8982.40     333.52
3  -11  -25    5262.34     213.70
4  -11  -25    9965.71     355.32
5  -11  -25    3268.04     153.98
6  -11  -25      51.35     104.90
-12  -10  -36    5181.97     282.02
-12  -10  -35    4733.18     169.19
-12  -10  -34    1109.44      63.70
-11  -10  -33     507.09      45.80
-11  -10  -32    4440.15     157.26
-10  -10  -31    4270.10     150.58
-10  -10  -30    2413.44      97.23
-9  -10  -29   11183.40     155.17
-8  -10  -28    4817.04     169.19
-8  -10  -27    7440.86     269.05
-7  -10  -27    6437.52     221.92
15  -10  -27    3707.00     155.48
-7  -10  -26     323.80      67.24
-6  -10  -26   21892.55     741.16
14  -10  -26    2348.42     106.54
15  -10  -26    2474.17      98.65
-6  -10  -25    1198.91      93.75
-5  -10  -25    8666.82     296.97
12  -10  -25   27257.46     973.02
13  -10  -25    2118.62      82.12
14  -10  -25    1323.67      82.42
-4  -10  -24    4431.26     161.98
-3  -10  -24   16273.77     560.37
11  -10  -24   18978.18     662.34
12  -10  -24    7748.80     278.83
13  -10  -24    5453.17     219.49
-3  -10  -23    7235.79     263.68
-2  -10  -23     802.58      53.77
-1  -10  -23   45407.49    1569.84
0  -10  -23   18612.28     639.94
8  -10  -23   53451.69    1847.52
9  -10  -23   20646.06     714.61
10  -10  -23    1123.14      74.18
11  -10  -23   10312.41     360.51
0  -10  -22   22888.74     783.14
1  -10  -22   12070.00     145.15
2  -10  -22    3679.68      91.57
3  -10  -22   21884.09     260.46
4  -10  -22    4280.94     132.05
5  -10  -22    3017.58      81.91
6  -10  -22    8505.74     171.97
7  -10  -22   27669.63     332.33
8  -10  -22   10857.37     156.01
9  -10  -22   16206.26     564.31
-14   -9  -33    3878.81     147.67
-14   -9  -32     653.46      43.52
-13   -9  -30     570.84      38.88
-12   -9  -28    4642.39     164.93
-11   -9  -27    8460.13     296.39
-10   -9  -26   40412.95    1438.20
-10   -9  -25    1653.66      77.68
17   -9  -25    8968.77     322.32
18   -9  -25    7472.78     126.00
-9   -9  -24    5751.95     200.89
16   -9  -24    7641.11     286.93
17   -9  -24    2966.41      94.44
-8   -9  -23     633.83      51.51
15   -9  -23    4200.66     170.07
16   -9  -23   14631.99     188.44
-7   -9  -22    1284.47      81.29
-6   -9  -22   13996.39     480.77
14   -9  -22    5026.35     183.01
15   -9  -22    8682.98     126.32
-5   -9  -21   20894.89     218.82
12   -9  -21    1528.03      92.93
13   -9  -21    1946.22      70.58
14   -9  -21      81.81      66.27
-3   -9  -20    6240.22      79.46
-2   -9  -20   23233.36     804.18
10   -9  -20    3638.17     133.43
11   -9  -20    5888.01     114.20
12   -9  -20   11336.57     388.03
-1   -9  -19    2407.82      98.28
0   -9  -19    1747.79      56.96
1   -9  -19    3286.75     106.71
2   -9  -19   36528.48    1087.50
6   -9  -19   29421.28     881.52
7   -9  -19   18519.35     551.46
8   -9  -19    9093.89     173.82
9   -9  -19    1170.60      57.95
3   -9  -18   15377.20     462.00
4   -9  -18   15740.54     462.48
5   -9  -18   22376.44     664.78
6   -9  -18   16079.97     481.17
-16   -8  -30     296.91      46.57
-15   -8  -29    6282.32     239.82
-15   -8  -28     224.56      46.23
-14   -8  -27    3205.82     126.79
-13   -8  -25    1037.10      50.81
20   -8  -24   12068.99     423.79
-12   -8  -24    3244.72     119.03
19   -8  -23   15281.12     535.52
20   -8  -23   10278.23     370.81
-11   -8  -23    5951.41     212.07
18   -8  -22    1997.37     107.76
19   -8  -22   15611.47     543.19
-9   -8  -21   12071.75     416.76
17   -8  -21    6225.79     231.39
18   -8  -21     869.31      72.87
-8   -8  -20    7290.29     252.19
16   -8  -20    2545.37     106.41
17   -8  -20    7948.16     281.89
-7   -8  -19    7410.10     252.11
15   -8  -19    5129.87      86.19
16   -8  -19    6519.15     243.84
-5   -8  -18   39159.09    1347.78
13   -8  -18   39628.69    1156.93
14   -8  -18     398.30      47.13
-4   -8  -17   25745.32     873.87
-3   -8  -17   24480.31     824.88
11   -8  -17   50270.65     638.15
12   -8  -17   16861.46     495.83
-1   -8  -16   58788.70    1732.05
0   -8  -16   18581.14     204.92
1   -8  -16   83081.90    2481.74
2   -8  -16   32050.50     960.07
6   -8  -16   10406.34     338.93
7   -8  -16     877.67      58.82
8   -8  -16   11052.05     229.37
9   -8  -16   22544.32     272.98
10   -8  -16    9366.86     298.74
-17   -7  -28    2550.94     110.21
-17   -7  -27    2270.95      93.55
-16   -7  -26      67.23      45.06
-15   -7  -24   14708.41     498.85
22   -7  -23    1880.45     102.25
21   -7  -22    2432.59     151.15
22   -7  -22     615.03      76.76
21   -7  -21    2002.95      85.54
20   -7  -20    9919.15     118.85
-12   -7  -20    1729.53      57.49
19   -7  -19    4908.11     108.17
-11   -7  -19    6176.80     172.95
17   -7  -18    5906.45     230.05
18   -7  -18   18194.01     238.69
-8   -7  -17   15224.98     433.60
16   -7  -17    4590.14     139.84
17   -7  -17     342.91      57.28
-7   -7  -16   17517.65     491.43
15   -7  -16   12683.10     174.16
-5   -7  -15   10824.01     298.99
13   -7  -15   23406.64     263.74
14   -7  -15    6459.36     204.09
-3   -7  -14   15769.40     347.06
-2   -7  -14   54100.59    1601.64
10   -7  -14   74877.98    2234.12
11   -7  -14   39909.22     638.15
1   -7  -13   13004.25     381.21
2   -7  -13   63716.62     723.85
3   -7  -13  137214.83    2429.57
4   -7  -13  117950.97    1980.04
5   -7  -13   59963.08     594.79
6   -7  -13   12907.29     166.40
8   -7  -13   21072.94     636.42
-18   -6  -25     635.84      45.69
24   -6  -22     568.54      64.39
-16   -6  -22   17988.75     760.69
23   -6  -21   13293.58     515.83
24   -6  -21    1232.89      80.21
23   -6  -20    2226.97      92.73
22   -6  -19    6738.27     113.53
21   -6  -18    5872.35     121.81
-13   -6  -18     726.65      37.87
20   -6  -17   11687.84     168.68
19   -6  -16    3091.32      85.32
17   -6  -15     985.31      57.87
18   -6  -15   24255.91     579.84
16   -6  -14    5748.06     110.38
-8   -6  -14    5180.53     144.45
-6   -6  -13   18587.48     526.21
14   -6  -13    7788.87     114.88
15   -6  -13    1182.48      83.97
-4   -6  -12   27348.91     610.27
11   -6  -12    8786.47     268.00
12   -6  -12   37638.83     480.61
-1   -6  -11    5442.49     127.22
0   -6  -11     211.94      22.83
1   -6  -11   11326.40     267.08
7   -6  -11    4358.02     146.47
8   -6  -11   21224.35     265.52
9   -6  -11   32507.83     995.29
-19   -5  -23    1409.80      68.19
26   -5  -21    7854.94     141.98
25   -5  -20    9237.18     346.60
-17   -5  -20    6422.53     266.04
24   -5  -19   12062.35     442.54
25   -5  -19    2435.45     135.85
24   -5  -18    1503.33      85.54
23   -5  -17   11914.59     446.15
22   -5  -16    8503.19     320.49
21   -5  -15    4957.42     193.53
19   -5  -14   12945.25     315.62
20   -5  -14    5011.43     137.29
18   -5  -13    2578.47      64.32
-10   -5  -13    2661.69      78.60
16   -5  -12   32496.99     976.61
17   -5  -12    4365.06     115.31
15   -5  -11    6294.15     106.07
-4   -5  -10   42140.28     959.48
12   -5  -10   32927.38    1008.05
13   -5  -10   10478.51     316.27
-1   -5   -9    8126.88     163.58
8   -5   -9   24741.28     814.11
9   -5   -9   46441.16     585.00
10   -5   -9    9027.77     283.80
27   -4  -20    2680.21     122.54
27   -4  -19    1508.03      88.89
26   -4  -18     444.34      85.35
25   -4  -17     968.17      83.91
24   -4  -16    3101.69     130.72
-16   -4  -16   22459.14     655.10
23   -4  -15   17561.49     632.83
22   -4  -14   10691.12     262.42
21   -4  -13    3994.26     107.74
-13   -4  -13   23259.69     666.33
20   -4  -12    3989.15      78.08
18   -4  -11   10463.02     271.46
19   -4  -11     878.53      49.95
17   -4  -10   11197.40     169.71
15   -4   -9    8805.12     129.16
-7   -4   -9   44270.89    1316.81
12   -4   -8   31024.80     948.80
13   -4   -8   24601.33     752.77
-1   -4   -7    1667.26      31.88
9   -4   -7   26971.36     367.15
10   -4   -7    9158.12     275.85
29   -3  -19     357.21      63.79
28   -3  -18    4820.20     121.53
27   -3  -17    3290.09     130.87
26   -3  -16    8874.89     348.66
26   -3  -15    5136.14     212.17
25   -3  -14    3667.67     148.50
24   -3  -13    1095.00      78.36
23   -3  -12    4276.56     117.28
21   -3  -11   13274.02     336.56
22   -3  -11   17961.97     453.74
20   -3  -10    1781.09      58.36
19   -3   -9   23044.10     579.12
17   -3   -8    1755.77      57.35
15   -3   -7   41300.59     485.51
12   -3   -6   96713.95    2995.25
13   -3   -6   27114.50     833.13
0   -3   -5   71133.23    1739.51
8   -3   -5   12972.55     301.71
9   -3   -5    2105.84      54.98
30   -2  -18     820.54      63.27
29   -2  -17    3027.84     122.27
28   -2  -16   13022.61     521.41
28   -2  -15    3694.06     167.48
27   -2  -14     828.54      60.39
26   -2  -13    1820.31      72.56
25   -2  -12    9430.83     148.87
24   -2  -11    1522.40      65.27
23   -2  -10    2995.56      83.14
22   -2   -9    5796.86     168.33
20   -2   -8    4853.67     136.27
19   -2   -7   11460.11     324.02
17   -2   -6    6723.75     184.17
15   -2   -5   11909.24     307.97
12   -2   -4   11222.38     261.77
1   -2   -3    2526.90      62.15
2   -2   -3   20234.70     501.61
6   -2   -3    2468.15      62.21
7   -2   -3   61992.11    1478.16
31   -1  -17      21.54      47.98
30   -1  -16     938.19      61.65
29   -1  -14    3085.00     134.81
28   -1  -13    1585.67      74.96
27   -1  -12    5370.57     111.79
26   -1  -11     489.83      36.70
25   -1  -10     735.07      55.68
24   -1   -9    1218.74      59.86
23   -1   -8     587.28      40.34
21   -1   -7   46812.67    1170.49
20   -1   -6   23171.68     591.01
18   -1   -5     824.22      42.18
16   -1   -4   88304.35    2324.01
14   -1   -3   86305.63    2066.57
11   -1   -2     595.46      25.14
32    0  -17    3505.67     162.46
32    0  -16     258.75      47.28
31    0  -15     162.52      45.70
30    0  -14    1242.16      98.97
30    0  -13    2636.49     131.37
29    0  -12    3065.61     122.93
28    0  -11    1091.00      65.57
27    0  -10    5699.67     175.38
26    0   -9    1864.88      59.91
25    0   -8    8073.54     120.38
24    0   -7   13426.69     333.41
21    0   -5     735.16      36.29
18    0   -3    1862.37      79.11
13    0   -1   52238.95    1262.30
8    0    0   19844.51     480.49
33    1  -16     438.31      66.85
33    1  -15     111.24      61.87
32    1  -14    1989.50      73.84
31    1  -13    2183.41     103.28
-23    1  -13   11732.39     508.57
30    1  -11     348.12      55.33
29    1  -10     959.71      49.90
28    1   -9    -108.13      34.73
27    1   -8     576.92      41.52
26    1   -7    4268.04     135.62
25    1   -6    3354.23     125.84
22    1   -4   21521.68     540.50
19    1   -2    3496.99     103.11
17    1   -1   12508.45     304.78
14    1    0   77353.80    1885.14
-6    1    0     177.51       8.62
11    1    1   11816.62     285.20
33    2  -13     392.72      51.63
32    2  -12    3891.32     155.16
31    2  -11     739.75      67.94
-23    2  -11     614.48      51.58
30    2   -9     414.66      67.76
29    2   -8     333.63      51.70
28    2   -7    1622.13      79.74
27    2   -6     864.63      74.51
24    2   -4    2232.33      74.37
-16    2   -4    4705.11     129.61
23    2   -3     472.92      29.68
20    2   -1   10184.06     238.88
18    2    0    5715.46     133.68
-4    2    2   32204.17     782.73
1    2    3    3339.38      80.32
-26    3  -13    4056.96     179.45
32    3  -10    3679.16     144.69
31    3   -9    1019.91      54.57
-23    3   -9   10521.94     434.55
30    3   -8    3445.77     128.83
-22    3   -8   19004.69     805.23
-19    3   -5    6913.75     196.39
26    3   -4   10802.29     341.49
-18    3   -4    6274.54     180.71
25    3   -3   14374.89     441.67
22    3   -1   41533.16    1021.70
-14    3   -1    5240.57     151.54
-8    3    2    3018.12      73.96
-1    3    4   10209.25     249.82
-26    4  -11    6543.01     256.20
31    4   -7     302.68      32.18
30    4   -6     288.23      32.59
29    4   -5     595.83      35.78
-21    4   -5    2682.46      80.03
28    4   -4     891.86      46.02
27    4   -3    3115.82     116.09
-16    4   -1   29362.99     748.95
23    4    0    1891.94      94.45
21    4    1   23055.55     513.08
-13    4    1   95222.98    2507.66
-11    4    2   43958.10    1026.87
-9    4    3    1832.99      68.83
-6    4    4   57439.66    1390.41
-25    5   -8    8186.41     323.96
-24    5   -7   12027.42     470.68
-19    5   -2   18477.87     457.19
26    5   -1   19649.48     596.47
-18    5   -1    9468.22     239.99
25    5    0    1316.44      56.54
-15    5    1   58554.98    1532.40
20    5    3    4085.32      95.27
-12    5    3    1132.37      55.49
-7    5    5    3897.10      85.65
-4    5    6   15226.20     380.72
-27    6   -9    1144.61      64.40
-23    6   -4    4099.55     159.04
30    6   -3    6619.79     213.97
-22    6   -3   11486.85     286.08
29    6   -2     327.25      30.35
-21    6   -2    4333.33     122.45
28    6   -1    1178.03      53.62
-17    6    1   17951.75     470.36
24    6    2    1104.72      69.38
-14    6    3    4247.48      78.21
-12    6    4   24946.39     589.88
-10    6    5   53746.49    1010.12
-8    6    6    7529.25     200.82
-4    6    7     885.26      29.81
2    6    8    1620.56      43.20
3    6    8   42759.18    1032.35
4    6    8   51589.00    1249.48
5    6    8  146997.70   -3241.80
6    6    8    2929.87      71.13
-26    7   -6   10342.66     425.27
-25    7   -5    8769.80     354.02
-24    7   -4   27392.70    1107.43
-22    7   -2    6059.19     154.05
-21    7   -1   38423.86     935.19
-20    7    0   21051.67     312.10
27    7    1    1064.04      55.38
-19    7    1   11001.36     281.79
-16    7    3   17103.01     191.46
-14    7    4   27082.29     652.19
-8    7    7    7754.55     117.56
0    7    9   16307.55     390.52
1    7    9    8922.07     174.42
2    7    9    2623.56      65.06
6    7    9    6436.84     155.50
7    7    9   28431.81     700.10
-28    8   -7    6169.25     254.54
-27    8   -6     501.20      54.04
-19    8    2   20529.61     490.64
26    8    3    1251.24      61.47
-18    8    3    2228.08      74.81
-16    8    4   42717.91    1059.89
-15    8    5   29729.52     772.88
-13    8    6   52152.05    1193.39
-11    8    7   21365.73     501.01
-8    8    8   61202.68    1492.23
-5    8    9    3898.96      96.56
0    8   10   17784.38     425.31
1    8   10   14184.31     338.18
2    8   10   26721.40     642.38
7    8   10  106545.82    2658.22
8    8   10     739.27      25.65
-29    9   -7    5046.46     201.69
-26    9   -3    5818.11     227.07
-25    9   -2    1974.61      89.97
-24    9   -1      75.36      31.61
-23    9    0   11838.38     270.15
-22    9    1     248.48      43.21
-19    9    3    7232.22     181.20
-18    9    4    8483.40     124.92
23    9    6     104.96      30.05
-15    9    6    6208.98     136.36
-13    9    7   29720.32     492.74
-11    9    8   57957.02    1279.97
-8    9    9   21884.88     521.01
-5    9   10     825.60      39.56
0    9   11     608.66      27.66
1    9   11   35691.18     868.91
2    9   11   50369.63    1237.60
7    9   11   12880.58     311.13
8    9   11   61360.30    1480.13
-28   10   -4    4133.70     176.41
-27   10   -3    1550.82      73.95
-26   10   -2     302.07      47.54
-25   10   -1    6337.33     240.53
-24   10    0    1059.76      43.96
-23   10    1    3978.13      94.43
-22   10    2    4009.96     101.73
-21   10    3    7141.72     173.48
-18   10    5    5748.34     139.19
-15   10    7   14477.77     286.24
-13   10    8     691.65      55.44
-11   10    9   12495.83     216.66
-8   10   10   28426.72     656.74
-5   10   11   58288.88    1130.62
13   10   11    3741.85      84.79
0   10   12   10631.02     261.61
1   10   12   13203.95     200.52
2   10   12    7350.11     177.13
3   10   12   81460.76    2001.55
5   10   12   83497.91    2084.23
6   10   12     258.70      30.21
7   10   12   11519.42     279.42
8   10   12   17314.43     404.20
-29   11   -4    2116.66      95.02
-28   11   -3    1966.12      81.88
-27   11   -2    1687.66      85.91
-26   11   -1    9685.82     353.03
-23   11    2     279.23      47.78
-22   11    3   12036.30     255.64
-21   11    4    5148.64     123.44
-18   11    6     532.68      37.28
-17   11    7    5452.85     147.67
-15   11    8    6485.11     146.54
-13   11    9   10666.14     266.11
-11   11   10    1234.94      61.25
-8   11   11   42224.96     588.56
-5   11   12     604.53      44.84
-4   11   12   26442.33     624.50
13   11   12     578.75      21.23
0   11   13    8137.08     206.27
1   11   13   43085.04    1054.97
2   11   13    5540.69      81.07
3   11   13   80492.20    1995.64
4   11   13  106217.99    2654.54
5   11   13    4454.65     116.99
6   11   13     908.12      33.92
7   11   13   54099.20    1288.77
-30   12   -4    1937.30     124.36
-29   12   -3    1335.81     102.84
-28   12   -2     180.70      95.14
-22   12    4    7995.61     173.30
-21   12    5    8670.11     154.80
-20   12    6    6253.75     162.00
-18   12    7     309.23      35.84
-17   12    8   26068.67     631.09
-15   12    9   12815.21     316.17
-13   12   10   11574.17     279.03
-11   12   11    9603.47     215.34
16   12   12    9334.08     356.84
-5   12   13    4755.24     122.79
-4   12   13   15616.95     336.08
2   12   14   31167.12     741.68
3   12   14   45605.31    1109.63
4   12   14   32557.43     809.03
5   12   14   20936.03     523.98
6   12   14     225.21      35.46
-31   13   -4     388.49      85.02
-30   13   -3    1148.09      98.44
-29   13   -2    4482.86     266.75
-22   13    5     507.59      77.31
-21   13    6    9168.69     152.54
-20   13    7   12780.03     532.75
-18   13    8    3592.73     101.38
-17   13    9   12603.06     446.04
-15   13   10    9811.46     210.73
-13   13   11    3058.68      76.47
-11   13   12    8371.15     200.05
-10   13   12   27515.34     609.16
16   13   13    4356.26     177.97
-8   13   13    7469.62     179.03
-7   13   13   20318.33     470.66
-4   13   14    5796.48     158.67
-3   13   14   81955.66    1852.54
12   13   14   11808.25     247.51
-31   14   -3     199.31      66.15
-30   14   -2    2086.42     151.62
-22   14    6    8213.06     337.77
-21   14    7   19033.11     321.40
-18   14    9    5833.72     142.52
-16   14   10   13555.56     458.66
-15   14   11    8123.93     287.78
-14   14   11    2176.72     122.09
-13   14   12    8553.27     293.55
-12   14   12    2727.83      77.57
-10   14   13    4494.79     103.41
-7   14   14   53540.18     811.15
15   14   14    6978.93     266.48
-3   14   15   81607.39    1679.04
-2   14   15    3635.01      89.80
11   14   15   10396.66     216.57
-31   15   -2    2305.11     152.98
-30   15   -1    3511.55     218.33
-27   15    3    1715.90     194.05
-23   15    6    5131.03     223.57
-22   15    7    5020.39     124.17
-21   15    8    3466.62     160.75
-19   15    9    1767.58     123.41
-18   15   10   10055.84     413.91
-16   15   11   35406.02     524.48
-14   15   12    7625.68     254.29
-12   15   13    1816.91      79.63
18   15   14    7160.02     283.07
-10   15   14    1447.08      74.78
-9   15   14    4560.88     117.75
-7   15   15    7477.59     171.48
-6   15   15    1094.54      75.03
-2   15   16     268.64      33.81
-1   15   16    4333.11     113.48
0   15   16     278.45      44.75
9   15   16    6854.34     153.49
10   15   16    5400.06     117.20
-32   16   -2    1291.83     111.84
-31   16   -1     578.23      67.83
-30   16    0   16464.55    1028.80
-23   16    7    6188.84     261.53
-22   16    8    1518.18      88.91
-21   16    9    1513.15     124.80
-19   16   10    7995.22     128.51
-18   16   11   10310.99     360.70
-16   16   12   22973.32     400.54
-14   16   13   14071.70     219.03
20   16   14     348.88      44.45
-12   16   14    7601.55     269.08
-11   16   14    2341.57     129.02
17   16   15    3527.73     149.95
-9   16   15    2970.52      86.58
-6   16   16   32940.02    1111.88
-5   16   16    8684.35     185.25
14   16   16    2005.71     104.60
-1   16   17    4708.20     115.47
0   16   17    1383.35      44.58
1   16   17    5020.07     109.83
2   16   17   11656.58     244.76
3   16   17    2174.36      61.78
4   16   17   17102.08     368.86
5   16   17    3637.02      90.25
6   16   17     601.39      32.11
7   16   17    3074.28      69.26
8   16   17    9380.21     194.18
9   16   17     437.37      42.24
-32   17   -1     691.02      80.05
-31   17    0     593.54      86.76
-30   17    1    3042.30     206.89
-24   17    7    2090.01     114.66
-23   17    8   13744.01     276.62
-22   17    9     263.20      70.10
-20   17   10    6082.21     268.97
-19   17   11    3586.82     102.90
-17   17   12    9323.83     316.44
-16   17   13    1160.91     121.35
-15   17   13   12363.69     427.16
-14   17   14     200.40     107.09
-13   17   14   19046.86     642.23
19   17   15    7985.36     308.01
-11   17   15     465.36      60.57
-8   17   16    3759.69     101.29
16   17   16    1786.38      96.45
-5   17   17    4292.91     146.98
-4   17   17    5327.14     125.52
-3   17   17    6986.24     168.74
12   17   17   13189.11     545.67
13   17   17    6620.86     299.48
2   17   18    6186.07     144.66
3   17   18    2694.61      74.01
4   17   18   20185.64     408.59
5   17   18    3981.77      94.72
6   17   18   14002.58     283.33
-26   18    6    2014.52     122.68
-25   18    7     714.43      76.23
-24   18    8    3077.63     121.58
-23   18    9    3577.26     163.70
-22   18   10     529.72     133.53
-21   18   10    2436.07     181.52
-20   18   11    9422.83     170.23
-19   18   12    3264.23     154.65
-18   18   12    6243.01     227.42
-17   18   13    1520.47      89.92
-15   18   14   11325.79     150.57
-13   18   15    3552.05     104.00
-10   18   16     570.14      73.58
-8   18   17   15787.69     550.16
-7   18   17    8758.71     132.79
15   18   17    2562.22     118.51
-4   18   18    3964.04     172.35
-3   18   18    1590.64      74.51
-2   18   18    2446.28      99.32
-1   18   18    2193.23     149.59
10   18   18    7843.92     153.20
11   18   18    3017.38      65.36
-21   19   11    3154.20     110.53
-20   19   12    4936.70     228.71
-18   19   13    2312.73     106.79
-16   19   14     469.40      64.23
-14   19   15    8952.23     317.72
-12   19   16   10918.50     201.59
-10   19   17    -236.28      72.00
-9   19   17    2578.54      97.39
-7   19   18    2556.95     147.21
-6   19   18    1957.78      92.28
-5   19   18   10919.65     372.93
14   19   18    1127.13      66.24
-2   19   19    9169.34     412.18
-1   19   19    7469.20     311.66
0   19   19   18936.53     254.80
1   19   19    8411.79     364.21
2   19   19   13985.28     271.29
3   19   19    5042.19     114.77
4   19   19   34417.88     648.63
5   19   19   18129.96     354.43
6   19   19    4168.62      92.35
7   19   19    6871.33     129.22
8   19   19     211.40      29.36
9   19   19    5239.12     103.04
-17   20   14    6949.07     264.32
-16   20   15     233.90      57.67
-14   20   16    7941.07     283.79
-13   20   16    5684.63     224.11
-11   20   17    6931.01     125.77
-9   20   18   20021.54     671.29
-8   20   18   10198.18     177.73
16   20   18    9242.56     394.86
-5   20   19    6524.98     221.05
-4   20   19    3329.68     100.23
-3   20   19    9837.37     330.41
12   20   19    9851.71     386.45
13   20   19    4819.81     210.98
2   20   20   17587.64     789.00
3   20   20    1291.04     103.26
4   20   20     956.61      91.56
5   20   20    5867.19     115.94
6   20   20    1855.41      67.74
-13   21   17    1191.07      90.99
-12   21   17    5705.42     239.90
-11   21   18    2410.46     136.26
-10   21   18   20797.01     390.21
-8   21   19    6020.33     222.46
-7   21   19   12571.20     200.25
-6   21   19   10026.40     338.03
15   21   19    2754.57     130.50
-3   21   20    1008.15      94.86
-2   21   20    3583.58     112.34
-1   21   20   28630.62    1227.26
0   21   20     184.23     129.25
9   21   20    2342.21      66.05
10   21   20   10161.36     389.06
11   21   20   13222.40     508.75
-11   22   18    3411.91     167.19
-10   22   19   11138.78     406.34
-9   22   19    5105.31     154.75
-8   22   19    6765.55     255.67
17   22   19    1873.29      90.99
-6   22   20    5950.59     200.00
-5   22   20     652.93      83.45
-4   22   20    4285.18     169.61
13   22   20    3296.10     141.94
14   22   20     531.57      58.78
-1   22   21   13586.98     635.83
0   22   21    2126.88     119.80
1   22   21   18636.11     191.75
2   22   21   12683.30     168.60
3   22   21   10670.93     154.73
4   22   21   19615.35     313.41
5   22   21   12290.03     204.34
6   22   21    8722.90     163.02
7   22   21    6219.16     262.15
8   22   21    1173.40      85.57
-7   23   20     501.82      63.83
16   23   20     356.07      44.65
-4   23   21    8147.39     379.73
-3   23   21     340.45      83.03
-2   23   21    2010.61     135.73
10   23   21   17665.62    1038.67
11   23   21    1620.03      78.68
12   23   21     517.57      61.85
14   24   21    1432.76      72.27
-1   24   22   11819.41     533.44
0   24   22    3361.25     114.90
1   24   22   15867.45     232.06
2   24   22    1717.18      99.47
3   24   22    7959.95     326.35
4   24   22   13301.72     539.55
5   24   22    1882.08     107.81
6   24   22    1786.78     103.20
7   24   22    3519.44     133.78
8   24   22     788.70     111.59
9   24   22     847.29     130.39
-2   25   22    5078.81     265.74
11   25   22     687.65     106.45
12   25   22    4090.61     252.66
13   26   22     872.15     161.54
1   26   23    2879.90     127.43
2   26   23    6051.95     183.46
3   26   23      23.19      64.01
4   26   23    4830.29     205.52
5   26   23    1144.21      82.36
6   26   23    5564.08     339.18
7   26   23      39.08      96.17
8   26   23    2263.90     158.38
9   26   23    3510.33     225.62
10   27   23    1814.51     174.23
11   27   23    1818.09     134.40
12   27   23    3750.26     234.30
6   28   24    4839.70     191.15
7   28   24    2498.34     171.54
8   28   24     242.75     101.15
9   28   24    2184.34     235.84
8   29   24    8005.03     502.79
9   29   24     926.52     154.72
10   29   24    1306.07     118.65
11   29   24     326.67      90.03
</value>
            </bestfileHKL>
            <bestfilePar>
                <value># parameter file for BEST 
TITLE          .
DETECTOR       ADSC
SITE           Not set
DIAMETER         209.72
PIXEL          0.1024000
ROTAXIS        0.00 0.00 1.00 FAST
POLAXIS        0.00 0.00 1.00
GAIN               0.25
CMOSAIC            0.61
PHISTART          90.00
PHIWIDTH           1.00
DISTANCE         198.39
WAVELENGTH      0.93400
POLARISATION    0.95000
SYMMETRY       P222
UB             -0.008264  0.001266 -0.014851
            0.008851  0.012520 -0.003858
            0.009369 -0.008452 -0.005935
CELL              54.80    59.07    66.98  90.00  90.00  90.00
RASTER           19  21  14   6   7
SEPARATION      0.710  0.710
BEAM            102.509  104.839
# end of parameter file for BEST
</value>
            </bestfilePar>
            <experimentalConditionRefined>
                <beam>
                    <exposureTime>
                        <value>1.000000e+00</value>
                    </exposureTime>
                    <wavelength>
                        <value>9.340000e-01</value>
                    </wavelength>
                </beam>
                <detector>
                    <beamPositionX>
                        <value>1.025087e+02</value>
                    </beamPositionX>
                    <beamPositionY>
                        <value>1.048387e+02</value>
                    </beamPositionY>
                    <bin>
                        <value>2x2</value>
                    </bin>
                    <byteOrder>
                        <value>little_endian</value>
                    </byteOrder>
                    <dataType>
                        <value>unsigned_short</value>
                    </dataType>
                    <distance>
                        <value>1.983900e+02</value>
                    </distance>
                    <imageSaturation>
                        <value>65535</value>
                    </imageSaturation>
                    <name>
                        <value>ADSC Q210 bin 2x2</value>
                    </name>
                    <numberBytesInHeader>
                        <value>512</value>
                    </numberBytesInHeader>
                    <numberPixelX>
                        <value>2048</value>
                    </numberPixelX>
                    <numberPixelY>
                        <value>2048</value>
                    </numberPixelY>
                    <pixelSizeX>
                        <value>1.024000e-01</value>
                    </pixelSizeX>
                    <pixelSizeY>
                        <value>1.024000e-01</value>
                    </pixelSizeY>
                    <serialNumber>
                        <value>444</value>
                    </serialNumber>
                    <twoTheta>
                        <value>0.000000e+00</value>
                    </twoTheta>
                    <type>
                        <value>q210-2x</value>
                    </type>
                </detector>
                <goniostat>
                    <oscillationWidth>
                        <value>1.000000e+00</value>
                    </oscillationWidth>
                    <rotationAxis>
                        <value>phi</value>
                    </rotationAxis>
                    <rotationAxisEnd>
                        <value>9.100000e+01</value>
                    </rotationAxisEnd>
                    <rotationAxisStart>
                        <value>9.000000e+01</value>
                    </rotationAxisStart>
                </goniostat>
            </experimentalConditionRefined>
            <generatedMTZFile>
                <path>
                    <value>/users/svensson/dawb_workspace/workflows-id14eh4/edna-working-dir/ControlCharForReorientationv2_0-00000083/MXv1Characterisation/Integration/MOSFLMIntegrationv10-01/process_2_2.mtz</value>
                </path>
            </generatedMTZFile>
            <statistics>
                <RMSSpotDeviation>
                    <value>6.295800e-02</value>
                </RMSSpotDeviation>
                <iOverSigmaAtHighestResolution>
                    <value>6.404298e+00</value>
                </iOverSigmaAtHighestResolution>
                <iOverSigmaOverall>
                    <value>4.550684e+01</value>
                </iOverSigmaOverall>
                <numberOfBadReflections>
                    <value>2</value>
                </numberOfBadReflections>
                <numberOfFullyRecordedReflections>
                    <value>200</value>
                </numberOfFullyRecordedReflections>
                <numberOfNegativeReflections>
                    <value>42</value>
                </numberOfNegativeReflections>
                <numberOfOverlappedReflections>
                    <value>1</value>
                </numberOfOverlappedReflections>
                <numberOfPartialReflections>
                    <value>1511</value>
                </numberOfPartialReflections>
            </statistics>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>4.149451e+00</value>
                </maxResolution>
                <minResolution>
                    <value>4.149451e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>5.145932e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.625680e+05</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.676000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>15</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>3.599517e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.169370e+05</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.899000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>121</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>3.353515e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.643160e+05</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>4.847000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>15</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>3.526523e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.149800e+05</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.899000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>121</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>2.934117e+00</value>
                </maxResolution>
                <minResolution>
                    <value>4.149451e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>5.855032e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>8.289700e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>1.347000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>32</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>3.309000e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>7.299600e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>1.976000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>227</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>3.346990e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>7.927400e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.193000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>32</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>3.221658e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>7.134200e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>1.976000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>227</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>2.395700e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.934117e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>5.070490e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>3.329800e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>5.460000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>38</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>2.791527e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>2.144800e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>6.430000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>261</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>2.974848e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>3.067100e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>9.400000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>38</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>2.613465e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>2.023700e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>6.430000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>261</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>2.074739e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.395700e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>4.608528e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>2.038700e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.820000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>51</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>2.212949e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.519000e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>5.790000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>299</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>2.489272e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.984800e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>7.400000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>51</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>2.136638e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.492200e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>5.790000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>299</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>1.855704e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.074739e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>3.666038e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.305800e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.910000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>48</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>1.531807e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>6.643000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.250000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>304</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>2.064459e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.302400e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>5.540000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>48</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>1.591427e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>6.816000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.250000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>304</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>1.694018e+00</value>
                </maxResolution>
                <minResolution>
                    <value>1.855704e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>2.662199e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>7.849000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.650000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>10</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>1.127502e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>2.871000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.010000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>192</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>1.910859e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>8.297000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.770000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>10</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>1.212988e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>3.070000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.010000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>192</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>1.568357e+00</value>
                </maxResolution>
                <minResolution>
                    <value>1.694018e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>1.544998e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>3.989000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.180000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>4</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>9.368711e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>2.571000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.170000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>83</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>1.309022e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>4.733000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.030000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>4</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>1.053807e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>2.938000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.170000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>83</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>1.467063e+00</value>
                </maxResolution>
                <minResolution>
                    <value>1.568357e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>0.000000e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>0.000000e+00</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>0.000000e+00</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>0</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>6.404298e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.176000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>1.560000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>17</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>0.000000e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>0.000000e+00</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>0.000000e+00</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>0</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>7.415799e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.394000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>1.560000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>17</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <subWedgeNumber>
                <value>0</value>
            </subWedgeNumber>
        </integrationSubWedgeResult>
        <integrationSubWedgeResult>
            <bestfileDat>
                <value>   90.5036      61.75       3.42
75.4210      67.25       3.61
64.6479      70.25       3.71
56.5683      82.75       4.12
50.2843      85.25       4.19
45.2572      84.75       4.17
41.1443      88.25       4.28
37.7170      88.75       4.29
34.8171      88.00       4.27
32.3315      87.00       4.24
30.1775      88.25       4.28
28.2928      89.25       4.31
26.6299      87.00       4.24
25.1519      88.75       4.29
23.8295      86.25       4.22
22.6394      83.75       4.15
21.5628      86.75       4.23
20.5841      85.25       4.19
19.6905      84.25       4.16
18.8715      87.50       4.26
18.1181      83.25       4.13
17.4226      84.00       4.15
16.7788      83.00       4.12
16.1809      83.25       4.13
15.6244      84.25       4.16
15.1050      85.25       4.19
14.6192      82.75       4.12
14.1637      82.75       4.12
13.7359      83.50       4.14
13.3334      77.00       3.93
12.9538      84.75       4.18
12.5954      82.00       4.09
12.2564      78.75       3.99
11.9353      85.00       4.18
11.6307      80.25       4.04
11.3414      80.75       4.05
11.0662      83.00       4.12
10.8041      82.75       4.12
10.5543      79.00       3.99
10.3158      81.75       4.08
10.0880      78.25       3.97
9.8701      79.25       4.01
9.6615      76.00       3.90
9.4617      79.50       4.02
9.2700      80.75       4.05
9.0860      77.75       3.96
8.9093      75.00       3.87
8.7394      74.50       3.85
8.5759      73.00       3.81
8.4185      77.75       3.96
8.2669      72.50       3.79
8.1207      75.75       3.89
7.9796      75.50       3.88
7.8435      70.75       3.72
7.7120      74.00       3.84
7.5849      78.50       3.98
7.4619      76.75       3.93
7.3430      74.00       3.83
7.2279      75.00       3.87
7.1164      74.00       3.84
7.0083      74.75       3.86
6.9035      75.75       3.90
6.8019      78.50       3.98
6.7033      70.50       3.72
6.6076      75.50       3.89
6.5146      76.50       3.92
6.4243      77.00       3.94
6.3365      75.75       3.90
6.2511      79.50       4.02
6.1680      74.75       3.86
6.0872      78.00       3.97
6.0085      78.50       3.97
5.9319      78.50       3.98
5.8573      79.00       4.00
5.7846      80.75       4.05
5.7137      81.50       4.08
5.6445      81.75       4.08
5.5771      83.00       4.12
5.5113      82.00       4.09
5.4471      76.00       3.90
5.3845      84.00       4.15
5.3233      88.25       4.28
5.2635      86.25       4.22
5.2051      89.50       4.32
5.1480      87.75       4.26
5.0922      90.00       4.33
5.0377      89.25       4.31
4.9843      94.00       4.44
4.9322      93.75       4.44
4.8811      90.50       4.34
4.8311      95.00       4.47
4.7822      97.25       4.53
4.7343     102.00       4.66
4.6874     104.25       4.72
4.6415     103.25       4.70
4.5965     107.50       4.81
4.5524     111.75       4.92
4.5091     117.00       5.05
4.4668     123.00       5.20
4.4252     122.50       5.18
4.3845     119.50       5.11
4.3445     125.50       5.25
4.3053     125.25       5.25
4.2669     128.75       5.33
4.2291     118.75       5.08
4.1921     133.00       5.43
4.1557     142.75       5.65
4.1200     143.50       5.67
4.0849     143.75       5.67
4.0505     144.50       5.69
4.0167     149.00       5.79
3.9835     154.25       5.90
3.9508     158.75       5.99
3.9187     159.50       6.01
3.8872     166.00       6.14
3.8562     170.25       6.23
3.8257     170.50       6.23
3.7957     173.25       6.29
3.7663     178.50       6.39
3.7373     183.00       6.48
3.7088     183.00       6.48
3.6807     186.50       6.55
3.6532     179.75       6.42
3.6260     178.00       6.38
3.5993     183.50       6.49
3.5730     189.50       6.60
3.5471     184.00       6.50
3.5216     183.75       6.49
3.4965     188.25       6.58
3.4718     184.00       6.50
3.4475     185.00       6.52
3.4235     182.25       6.47
3.3999     183.25       6.49
3.3766     184.75       6.51
3.3537     177.75       6.38
3.3312     176.00       6.34
3.3089     170.00       6.22
3.2870     172.75       6.28
3.2654     166.25       6.15
3.2441     161.50       6.05
3.2231     158.00       5.98
3.2024     153.00       5.87
3.1820     151.50       5.84
3.1618     142.50       5.65
3.1420     144.00       5.68
3.1224     141.00       5.61
3.1031     138.50       5.56
3.0841     127.50       5.30
3.0653     127.50       5.30
3.0468     120.50       5.14
3.0285     120.00       5.12
3.0104     117.75       5.07
2.9926     116.50       5.04
2.9750     116.75       5.04
2.9577     112.75       4.94
2.9406     104.50       4.73
2.9237     105.00       4.74
2.9070     105.00       4.74
2.8905      99.50       4.59
2.8742      97.25       4.53
2.8582      94.00       4.44
2.8423      96.50       4.51
2.8267      89.50       4.31
2.8112      94.75       4.46
2.7959      89.00       4.30
2.7808      85.25       4.19
2.7659      86.75       4.23
2.7512      89.00       4.30
2.7366      86.75       4.23
2.7222      82.75       4.11
2.7080      85.75       4.20
2.6940      82.25       4.10
2.6801      83.50       4.14
2.6664      82.75       4.11
2.6529      84.25       4.16
2.6395      85.50       4.20
2.6262      82.00       4.09
2.6132      80.50       4.04
2.6002      84.25       4.16
2.5874      77.75       3.96
2.5748      83.00       4.12
2.5623      82.75       4.11
2.5499      79.75       4.02
2.5377      79.25       4.01
2.5256      80.50       4.04
2.5136      82.50       4.11
2.5018      80.75       4.05
2.4901      82.75       4.12
2.4785      81.50       4.08
2.4671      76.50       3.92
2.4558      82.25       4.10
2.4446      81.25       4.07
2.4335      72.50       3.79
2.4225      77.50       3.95
2.4117      83.00       4.12
2.4010      75.50       3.89
2.3903      80.50       4.05
2.3798      84.50       4.17
2.3694      79.50       4.02
2.3591      75.25       3.88
2.3489      84.25       4.16
2.3389      73.50       3.81
2.3289      77.00       3.92
2.3190      85.50       4.20
2.3092      82.75       4.11
2.2995      79.75       4.02
2.2900      86.75       4.23
2.2805      88.25       4.28
2.2711      83.25       4.13
2.2618      85.50       4.20
2.2526      79.25       4.01
2.2434      83.25       4.13
2.2344      87.75       4.26
2.2255      83.75       4.14
2.2166      89.25       4.31
2.2078      88.50       4.29
2.1992      86.75       4.24
2.1905      89.25       4.31
2.1820      87.50       4.26
2.1736      87.25       4.25
2.1652      89.00       4.30
2.1569      91.25       4.37
2.1487      86.25       4.22
2.1406      86.00       4.21
2.1326      85.25       4.19
2.1246      84.00       4.15
2.1167      91.75       4.38
2.1088      90.50       4.34
2.1011      85.50       4.20
2.0934      86.50       4.23
2.0858      83.00       4.12
2.0782      82.75       4.11
2.0707      86.50       4.23
2.0633      85.25       4.19
2.0560      84.25       4.16
2.0487      87.00       4.24
2.0415      80.00       4.03
2.0343      82.00       4.09
2.0272      84.00       4.15
2.0202      76.25       3.91
2.0132      77.50       3.95
2.0063      75.50       3.89
1.9995      71.50       3.76
1.9927      70.00       3.70
1.9859      70.50       3.75
1.9793      34.00       1.82
</value>
            </bestfileDat>
            <bestfileHKL>
                <value> -14    8  -39     725.98     105.31
-13    9  -38     196.42     105.14
-15    6  -37     529.66     122.38
-16    5  -36     201.47     121.42
-15    6  -36     297.34      80.30
-14    7  -36     452.74     107.43
-15    6  -35     524.03     119.94
-14    7  -35    8917.38     333.69
-13    8  -35     232.98      89.29
-12    9  -35    3653.99     216.33
-11   10  -35    1126.65     147.19
-10   11  -35     368.82     118.43
-9   12  -35     468.31     105.69
-16    4  -34    2345.17     164.71
-14    7  -34     246.53     144.79
-13    8  -34     417.09      97.84
-12    9  -34    2510.91     104.51
-11   10  -34    2638.76     102.33
-10   11  -34     887.52      95.87
-9   12  -34     805.35      95.60
-16    4  -33     634.84      74.17
-15    5  -33    2392.20     177.93
-11   10  -33     460.98     127.55
-10   11  -33     151.99     124.41
-9   12  -33     975.85     176.11
-17    2  -32    2382.04     149.12
-15    5  -32     394.87      84.70
-14    6  -32     999.04      97.73
-7   13  -32    2329.00     176.91
-6   14  -32   15692.80     374.75
-17    2  -31      57.13      72.79
-16    3  -31    5468.88     261.55
-14    6  -31     310.07     108.07
-13    7  -31    1292.10     100.97
-12    8  -31    1885.71     126.01
-11    9  -31    5492.06     280.08
-10   10  -31    5429.10     292.00
-9   11  -31    4083.19     230.80
-8   12  -31    3010.86     116.95
-7   13  -31     906.48     107.01
-6   14  -31    2263.45     169.44
-18    0  -30    1758.68      97.55
-16    3  -30    1303.93      89.65
-15    4  -30    2947.25     159.23
-12    8  -30     383.17     130.15
-11    9  -30    2783.36     174.75
-10   10  -30    2822.34     155.96
-9   11  -30    2198.09     141.71
-8   12  -30      -7.93     133.60
-4   15  -30    1398.32     125.39
-3   16  -30    4063.29     245.04
-17    1  -29    5743.33     249.00
-15    4  -29     399.39      98.60
-14    5  -29    3233.01     159.18
-6   13  -29    3300.72     206.68
-5   14  -29    6071.57     168.70
-4   15  -29    1330.80     156.60
-2   16  -29    3634.01     168.38
-18   -1  -28    1391.74      85.82
-16    2  -28    2345.40     126.88
-13    6  -28    1374.32     112.21
-12    7  -28    6416.10     130.80
-11    8  -28     254.53      55.87
-10    9  -28    1990.70     165.30
-9   10  -28    5355.46     290.80
-8   11  -28    2841.04     172.71
-7   12  -28    6623.62     143.22
-6   13  -28   10298.78     486.69
-3   15  -28     832.03     161.16
-2   16  -28    2862.80     136.41
0   17  -28   48833.89    1726.47
-19   -3  -27     729.98      65.51
-17    0  -27   25861.40    1157.15
-15    3  -27    1089.18      85.58
-11    8  -27     539.02      80.07
-10    9  -27    3728.27     225.06
-9   10  -27    1077.95     141.07
-8   11  -27     398.83     167.18
-4   14  -27    2079.46     149.72
-3   15  -27   12190.36     574.39
0   17  -27   40653.18     831.64
-18   -2  -26    9188.43     394.90
-16    1  -26    6839.10     308.82
-14    4  -26     568.04      99.39
-13    5  -26    6986.98     148.11
-6   12  -26     982.85     124.38
-5   13  -26    7188.22     126.25
-4   14  -26    2167.86     176.02
-2   15  -26     624.31     165.17
-1   16  -26   19078.59     299.09
1   17  -26   11107.03     423.76
2   18  -26    1481.95     110.57
-17   -1  -25    8299.89     369.52
-15    2  -25    2020.11     114.51
-12    6  -25    3300.41      96.98
-11    7  -25   11437.25     231.88
-10    8  -25    2960.05     110.99
-9    9  -25   22883.26     345.93
-8   10  -25     912.49      81.39
-7   11  -25    3983.28     189.83
-6   12  -25     251.89     140.92
-3   14  -25     206.18      97.54
-2   15  -25   11935.45     196.27
0   16  -25   55038.23    1947.86
1   17  -25    4682.51     169.99
3   18  -25    1322.26     107.68
-18   -3  -24   14721.58     640.56
-16    0  -24   16166.16     694.04
-14    3  -24     108.13      41.68
-13    4  -24    2843.59      82.84
-5   12  -24   22914.29    1045.88
-4   13  -24    1072.76      86.59
-3   14  -24    7450.93     288.60
-1   15  -24   20208.30     704.95
0   16  -24   15459.00     245.67
2   17  -24    8287.97     323.12
3   18  -24    2423.38     214.35
4   18  -24   14053.35     551.50
5   19  -24   12454.17     509.30
6   19  -24   16913.75     664.36
-17   -2  -23    8242.16     358.98
-15    1  -23    3769.40     169.62
-12    5  -23    8836.63     196.26
-11    6  -23    3812.58      90.48
-10    7  -23    3783.51      95.86
-9    8  -23   27017.79     596.05
-8    9  -23     260.99      46.75
-7   10  -23     730.12      47.38
-6   11  -23   13537.67     290.99
-5   12  -23    2706.79     179.16
-2   14  -23    7303.01     264.99
-1   15  -23   16773.91     593.29
1   16  -23   29416.46    1040.29
2   17  -23    2918.55     170.07
4   18  -23    2986.92     103.28
6   19  -23   15024.77     297.66
8   20  -23    1961.09     124.67
-16   -1  -22    5318.70     235.24
-14    2  -22    3304.60      95.63
-13    3  -22   35356.61     791.42
-4   12  -22    4233.99     114.72
-3   13  -22    2265.87      92.04
0   15  -22    2874.58     128.89
1   16  -22   14153.71     537.75
3   17  -22     542.68     104.73
5   18  -22    2576.35     104.88
7   19  -22      76.67      87.57
9   20  -22    2608.38     110.04
-18   -5  -21    1483.75      82.27
-12    4  -21    9735.35     244.83
-11    5  -21   50173.00     700.42
-10    6  -21    3870.23     105.30
-9    7  -21   28162.56     678.40
-8    8  -21   25329.45     620.50
-7    9  -21    4293.05     115.61
-6   10  -21    4151.52     122.56
-5   11  -21   36869.04     840.96
-1   14  -21    3780.73     116.48
2   16  -21    1020.68      86.74
6   18  -21    3716.20     162.57
8   19  -21    4184.01     137.39
10   20  -21    2214.82     116.26
-17   -4  -20   22311.16     922.70
-13    2  -20   17453.54     386.19
-3   12  -20     903.32      82.06
-2   13  -20    4055.51     101.98
1   15  -20    3288.24     112.68
3   16  -20   20568.44     752.55
5   17  -20   39195.34    1477.91
6   18  -20     233.42     164.03
7   18  -20    5070.31     228.52
9   19  -20    5309.69     200.42
11   20  -20    3289.64     158.63
12   20  -20   10501.02     409.43
-16   -3  -19    2686.36     115.60
-14    0  -19   18481.74     404.89
-11    4  -19    3469.14     101.62
-10    5  -19    4085.76     113.21
-9    6  -19   17383.62     441.41
-8    7  -19   11892.25     300.75
-7    8  -19   13762.76     340.61
-6    9  -19   23884.21     427.10
-5   10  -19   10993.22     221.49
-4   11  -19    3113.19     108.29
-1   13  -19    3712.93      93.97
0   14  -19   15104.88     325.79
2   15  -19   21851.22     364.55
5   17  -19    9814.08     375.39
7   18  -19    8137.95     313.43
8   18  -19   15232.11     577.68
10   19  -19   22883.29     334.61
12   20  -19    6202.66     239.09
13   20  -19    7387.34     308.62
15   21  -19    2514.38     152.71
16   21  -19    2637.21     101.90
-12    2  -18   10556.73     246.12
-3   11  -18    9008.74     200.41
-2   12  -18    1847.32      67.00
1   14  -18    8128.15     191.42
3   15  -18   13534.09     513.79
4   16  -18   10332.90     394.08
6   17  -18   17879.55     650.12
8   18  -18    3490.91     167.43
9   18  -18   30051.92    1096.64
11   19  -18    2800.22     114.24
13   20  -18     975.48     171.30
14   20  -18    6334.36     137.24
17   21  -18    1297.80      95.63
18   21  -18     977.13      84.01
-15   -3  -17    5249.46     118.58
-13    0  -17   89211.73    1999.95
-9    5  -17    8205.80     225.68
-8    6  -17   94277.52     699.24
-7    7  -17   53381.82     544.70
-6    8  -17   30127.51     395.88
-5    9  -17   39502.36     879.80
-1   12  -17   13185.01     291.20
0   13  -17   25353.69     562.10
2   14  -17   16125.05     346.20
5   16  -17    2654.79     127.49
7   17  -17    7675.46     280.15
9   18  -17    2894.58     145.91
10   18  -17    6552.71     258.32
12   19  -17    4760.51     118.54
15   20  -17     240.82      85.45
16   20  -17    6732.93     283.58
19   21  -17    2807.85     131.18
20   21  -17    3490.69     155.00
21   21  -17    9479.84     375.18
-20  -14  -16    1296.85      75.84
-11    2  -16    7641.82     186.36
-4    9  -16   78564.92    1766.31
-3   10  -16    6367.42     120.21
-2   11  -16   42570.24     978.91
1   13  -16    1748.62      80.45
4   15  -16    2021.07      80.05
6   16  -16   31167.24    1140.74
8   17  -16    3297.11     144.51
11   18  -16    1385.76      99.50
13   19  -16   13704.81     529.19
14   19  -16    8846.42     358.18
16   20  -16    1796.58     188.65
17   20  -16     761.88      90.32
18   20  -16   15910.04     626.24
21   21  -16    1901.35     113.78
22   21  -16      86.14      79.51
23   21  -16    1654.34     122.97
-14   -3  -15    4417.96     104.41
-12    0  -15    1104.12      39.63
-1   11  -15    1866.17      81.52
2   13  -15   14010.84     229.49
5   15  -15    9903.77     221.81
7   16  -15   14625.29     305.68
9   17  -15    1770.59     109.02
12   18  -15    1673.25      83.51
15   19  -15    2854.89     100.48
18   20  -15     538.50     137.32
19   20  -15    3733.60     112.38
20   20  -15    2114.25     116.66
25   21  -15     697.07     132.23
26   21  -15     452.31     115.71
-9    3  -14   39375.56    1020.30
-8    4  -14  119448.23    3186.10
-7    5  -14   57451.96    1525.80
-6    6  -14   81770.47    1959.09
-5    7  -14  104527.35    2494.56
-4    8  -14   50714.28     590.28
-3    9  -14   39593.46     949.58
0   11  -14    3806.04     116.27
1   12  -14    7745.65     189.88
3   13  -14   92778.57    2134.58
6   15  -14    2515.57      78.23
8   16  -14   11688.82     252.34
11   17  -14   12538.71     449.48
13   18  -14    3987.46     166.62
14   18  -14    3886.47     184.77
16   19  -14     499.35     132.75
17   19  -14     445.71      82.87
21   20  -14    1790.33     105.63
22   20  -14     326.74      85.45
23   20  -14     732.24     109.36
24   20  -14    1903.86     181.82
-20  -18  -13    5291.53     234.71
-19  -15  -13   15008.50     628.85
-10    1  -13   54000.41    1404.75
-2    9  -13   13760.10     166.50
-1   10  -13   17049.66     422.03
4   13  -13   14487.97     356.73
7   15  -13    6144.90     150.45
10   16  -13   16758.77     364.11
12   17  -13    3314.07      86.74
15   18  -13    8642.70     140.68
18   19  -13    2487.64     170.60
19   19  -13    1909.47      88.01
20   19  -13    5740.64     241.51
25   20  -13     487.10     120.88
26   20  -13     207.75      93.39
27   20  -13    2293.48     146.33
28   20  -13     579.40      96.57
-20  -20  -12    2671.88     134.54
0   10  -12   10551.91     178.31
3   12  -12   99166.91    2132.80
5   13  -12   96168.45    2205.30
11   16  -12   23188.12     535.19
13   17  -12    8841.61     221.88
14   17  -12   11237.11     265.07
17   18  -12   17055.20     248.29
21   19  -12    1756.68     108.29
22   19  -12    2079.62      98.46
23   19  -12    4396.47     225.90
24   19  -12    4180.77     277.17
-20  -22  -11    1286.67      81.59
-19  -18  -11    1524.49      90.29
-18  -15  -11    5466.25     237.95
-7    3  -11   52337.62    1223.69
-6    4  -11  140660.53    3323.02
-5    5  -11    4434.79     112.69
-4    6  -11   10835.53     214.40
-3    7  -11   24204.83     581.47
1   10  -11   23275.97     283.68
4   12  -11    8923.26     157.65
6   13  -11   25564.42     587.88
8   14  -11   20494.46     481.41
10   15  -11   19143.44     405.42
12   16  -11   13774.10     329.30
15   17  -11    3040.61      91.07
16   17  -11    7548.65     194.53
19   18  -11    2934.33     138.63
20   18  -11   10532.67     408.38
25   19  -11    3865.62     256.31
26   19  -11    2328.86     164.83
27   19  -11     447.58      94.07
28   19  -11     239.08      86.28
-20  -24  -10     454.18      74.47
-19  -20  -10    1351.10      90.14
-18  -17  -10   14497.34     582.80
-17  -14  -10    5500.39     227.43
-8    1  -10   30695.93     809.02
-2    7  -10   21504.82     407.40
2   10  -10   15087.62     372.08
5   12  -10   33528.16     477.39
7   13  -10   12441.70     198.01
9   14  -10   17613.46     321.98
11   15  -10    2846.28      82.88
14   16  -10    3361.98      83.99
17   17  -10    4625.25     119.77
18   17  -10   16737.59     356.50
22   18  -10     478.73     103.60
23   18  -10    7263.81     370.89
24   18  -10     729.38     109.91
25   18  -10    -302.11     161.82
-19  -22   -9    5932.24     286.66
-16  -13   -9    3358.94      74.25
-1    7   -9   16289.09     395.84
0    8   -9      97.18      23.84
3   10   -9    3655.97      93.30
6   12   -9    3877.59     104.34
8   13   -9   23400.55     545.66
10   14   -9    9042.75     208.19
13   15   -9    2836.51      81.99
16   16   -9    3205.25      86.89
20   17   -9   20606.67     361.37
21   17   -9   17274.04     352.86
28   18   -9    1183.95     172.03
-19  -26   -8    1157.97     123.61
-19  -25   -8    1745.08     101.96
-18  -21   -8       4.69     104.56
-17  -17   -8    5943.88     258.24
-15  -12   -8   11250.85     244.88
-14  -10   -8    4976.42     112.52
-9   -2   -8    3583.51      96.78
1    8   -8   15219.21     380.28
4   10   -8   56933.82    1167.99
12   14   -8   21377.65     543.88
15   15   -8     421.92      49.80
18   16   -8    4779.04     116.32
19   16   -8    9613.81     227.18
23   17   -8   10846.41     349.45
24   17   -8    1756.18      76.26
25   17   -8     372.23      51.38
26   17   -8    2562.01     160.59
27   17   -8     666.52     118.26
28   17   -8    6582.75     366.56
-19  -29   -7     904.19      72.72
-19  -28   -7     328.42      80.67
-18  -23   -7    5471.46     260.33
-17  -19   -7    1734.37     102.18
-16  -16   -7     458.53      30.03
2    8   -7   10173.45     243.55
5   10   -7    3530.38      87.99
7   11   -7   12241.88     293.14
9   12   -7    9642.51     236.39
11   13   -7   38495.29     506.59
14   14   -7   14410.75     379.52
17   15   -7   19604.12     461.28
21   16   -7    7977.66     178.58
22   16   -7    6918.78     239.72
-18  -27   -6      43.67      93.81
-18  -26   -6    2887.80     158.36
-18  -25   -6    1399.36     139.61
-17  -21   -6    2336.68     121.71
-16  -18   -6    1305.64      56.63
-15  -15   -6    3310.85      78.26
-11   -7   -6   19916.27     512.10
-4    2   -6    4372.66     107.51
-3    3   -6   14982.21     360.61
3    8   -6   18553.16     450.61
8   11   -6   37314.93     888.71
10   12   -6   41276.74    1078.89
13   13   -6    4544.27     135.74
16   14   -6   54182.51    1375.49
19   15   -6   10360.89     241.91
20   15   -6    8306.73     192.62
26   16   -6     571.14      67.56
27   16   -6    2638.10      98.97
28   16   -6    3534.30     123.88
-18  -33   -5     291.08      69.78
-18  -32   -5     584.86      72.82
-18  -31   -5     374.01      67.31
-18  -30   -5     597.15      73.74
-18  -29   -5     559.68     114.50
-17  -25   -5   10807.70     491.44
-17  -24   -5     543.39      70.57
-16  -20   -5     812.36      70.29
-15  -17   -5    4722.31     142.90
-13  -12   -5    8472.65     192.42
-12  -10   -5    9772.98     233.26
-5    0   -5   93379.91   -1946.61
-2    3   -5    2067.87      50.30
-1    4   -5   25948.43     622.86
3    7   -5   13465.04     323.19
6    9   -5    2339.73      54.31
12   12   -5   19694.67     257.38
15   13   -5    8560.49     232.17
18   14   -5     421.80      35.50
23   15   -5    7121.09     234.89
24   15   -5    2247.43      92.19
25   15   -5    2887.69     124.26
-17  -29   -4    2778.81     144.21
-17  -28   -4     543.23      66.27
-17  -27   -4     587.58      86.24
-16  -23   -4    5315.29     249.54
-16  -22   -4     475.42     100.05
-15  -19   -4    1567.40      63.51
-14  -16   -4    1269.08      53.18
-1    3   -4   13118.53     319.86
4    7   -4   21170.75     608.83
9   10   -4   11815.38     273.05
11   11   -4   56983.82    1488.42
14   12   -4     945.40      47.18
17   13   -4    1423.81      50.26
21   14   -4    7323.42     258.81
22   14   -4   22447.77     770.65
-17  -34   -3    -203.80      88.53
-17  -33   -3     519.17     103.97
-17  -32   -3    -230.12     130.43
-16  -27   -3    3596.12     204.83
-16  -26   -3    7744.50     351.36
-16  -25   -3     243.91      93.57
-15  -21   -3   22283.04     664.45
-14  -18   -3    1029.92      51.02
-12  -13   -3    8330.33     191.66
-11  -11   -3   30224.50     729.93
-8   -6   -3    7349.56     171.85
0    3   -3     187.20       9.06
7    8   -3    8103.22     186.06
11   10   -3   12578.73     322.75
13   11   -3    3902.49     108.96
16   12   -3    9038.07     226.03
20   13   -3    9827.12     236.84
27   14   -3     933.38      78.22
-16  -34   -2     460.68      76.16
-16  -33   -2    1600.18     104.25
-16  -32   -2     241.41      65.75
-16  -31   -2    1618.81     105.20
-16  -30   -2    1557.73      99.09
-16  -29   -2     550.97     103.39
-15  -25   -2   10754.95     326.49
-15  -24   -2     463.55      57.90
-14  -20   -2    5499.41     173.19
-13  -17   -2    7770.39     244.04
-12  -15   -2     958.78      70.88
-9   -9   -2  145763.36    3647.44
-4   -2   -2   32510.71     804.19
5    6   -2   25493.74     611.85
15   11   -2    7330.58     193.53
19   12   -2    2087.80      60.16
24   13   -2    4232.21     160.13
25   13   -2    1446.18      70.95
26   13   -2    6390.50     236.74
27   13   -2     420.16      58.44
-15  -31   -1    4023.35     214.82
-15  -30   -1     602.72      89.35
-15  -29   -1     840.65      83.34
-15  -28   -1     371.56      67.78
-15  -27   -1    2628.23     159.40
-14  -23   -1   19652.56     285.62
-13  -20   -1    9272.33     294.73
-13  -19   -1    7114.69     237.36
-12  -17   -1    7921.33     255.93
-11  -14   -1   24922.43     813.88
-10  -12   -1   10584.75     259.84
-7   -7   -1    2499.33      62.11
5    5   -1   40141.19     968.83
10    8   -1    2140.79      56.45
12    9   -1   15485.59     392.64
15   10   -1   24411.47     615.63
18   11   -1    5695.34     139.36
23   12   -1    1015.44      58.28
24   12   -1    8069.74     289.46
-14  -28    0     370.06      84.05
-14  -27    0   23515.94     428.01
-14  -26    0    7066.93     261.68
-13  -22    0    7047.70     124.35
-12  -19    0   10056.57     319.37
-11  -16    0   28587.59     934.88
-10  -14    0    1111.08      64.76
-9  -12    0   84499.65    2023.84
-8  -10    0   10052.78     227.09
-6   -7    0   31181.94     726.69
-2   -2    0    1075.90      25.86
8    6    0     119.26      12.77
12    8    0    4273.04     107.57
17   10    0    1258.20      53.60
22   11    0    1725.16      73.38
-14  -33    1     505.91      74.37
-14  -32    1     116.80      78.58
-14  -31    1     946.30     110.85
-13  -26    1     573.68      73.62
-13  -25    1    6347.34     207.66
-12  -22    1   11113.46     349.67
-12  -21    1    2662.23     106.07
-11  -18    1    4415.34     158.71
-10  -16    1    3498.42     119.90
-7  -10    1   12142.22     270.75
-5   -7    1   27810.17     658.75
8    5    1    7439.46     175.25
14    8    1    5720.23     143.86
17    9    1    7672.25     187.40
21   10    1    6566.63     220.50
-13  -33    2     235.10      76.22
-13  -32    2     149.18      73.39
-13  -31    2    1401.04      82.69
-13  -30    2    2021.23     100.92
-13  -29    2     793.72     105.78
-12  -25    2    1411.45      79.51
-12  -24    2    1064.43      81.66
-11  -21    2    6004.22     198.30
-10  -18    2    1660.42      60.47
-6  -10    2   38108.48     854.48
-4   -7    2   17073.27     407.15
20    9    2   11900.06     279.54
-12  -32    3    2148.30     108.23
-12  -31    3    1637.82      90.96
-12  -30    3    1073.70      77.24
-12  -29    3      17.05      62.53
-12  -28    3     921.11      98.63
-11  -25    3    3476.08     171.01
-11  -24    3     799.80      78.28
-10  -21    3    2432.88     107.46
-10  -20    3   10300.59     338.12
-9  -18    3    1413.93      74.62
-8  -15    3   55668.04    1817.13
-5  -10    3    4619.47     107.46
-3   -7    3   20698.29     472.06
20    8    3   26496.57     633.84
26    9    3    4695.02     184.60
27    9    3    2041.46      94.02
-11  -32    4    2437.85     159.19
-11  -31    4    2768.95     144.14
-11  -30    4     918.09      75.11
-11  -29    4    1746.92      87.08
-11  -28    4    5439.74     206.43
-11  -27    4    2022.18     141.38
-10  -24    4    4023.44     143.44
-10  -23    4   12241.44     390.66
-9  -20    4    4194.42     143.25
-8  -18    4   11073.28     360.20
-7  -15    4   18622.61     464.51
-6  -13    4    1072.07      76.42
-4  -10    4    6912.39     136.68
-1   -6    4   17598.01     276.51
4   -1    4   38834.68     938.54
26    8    4    1953.86      83.61
27    8    4    4426.72     180.78
-10  -30    5   10819.21     412.31
-10  -29    5    1034.87      79.36
-10  -28    5      21.44      79.75
-10  -27    5    4152.45     182.60
-9  -24    5    2577.94     117.73
-9  -23    5    2122.31      93.88
-8  -20    5    1366.20      63.63
-7  -18    5   38265.40     902.10
-7  -17    5   10595.25     280.86
-6  -15    5   18819.36     463.58
-3  -10    5   21182.48     484.03
2   -4    5   11270.83     291.16
26    7    5   14162.27     549.96
27    7    5   11077.36     452.64
-9  -30    6     433.01     108.61
-9  -29    6     -48.47      75.09
-9  -28    6    1336.19      89.08
-9  -27    6    7056.13     264.67
-8  -24    6    5051.01     196.07
-8  -23    6   20123.41     340.83
-7  -20    6    5725.83     134.53
-6  -18    6    2399.65      83.08
-3  -12    6   52569.25    1043.52
-1   -9    6    6594.39     147.33
-8  -30    7    4114.23     199.12
-8  -29    7   10381.72     381.47
-8  -28    7    5757.80     122.63
-8  -27    7    3781.06     163.91
-7  -24    7   20728.90     722.09
-7  -23    7    7385.34     149.40
-6  -21    7   12316.02     293.34
-6  -20    7   11212.09     224.40
-5  -18    7   12169.01     292.29
-4  -16    7   10251.40     256.63
-3  -14    7   18336.41     457.85
-2  -12    7   36617.12     926.43
1   -8    7   17868.18     412.25
2   -7    7   12361.55     258.01
3   -6    7    8109.75     190.97
4   -5    7   44587.74    1062.83
5   -4    7    6463.21     163.99
9   -1    7   55490.79    1459.89
-7  -30    8    1102.04     104.67
-7  -29    8    1513.86      98.73
-7  -28    8    2714.63     105.32
-7  -27    8     414.99      84.87
-6  -24    8    4977.85     174.24
-6  -23    8    4318.39     159.21
-5  -21    8    7248.93     178.53
-5  -20    8    5740.94     150.97
-4  -18    8   39503.88     642.79
-3  -16    8   35227.52     561.07
-2  -14    8    6804.00     175.53
0  -11    8   91820.32    2420.16
1  -10    8   39319.28     998.89
8   -3    8   38412.66     895.28
11   -1    8   82316.96    2182.89
-6  -30    9    6452.94     253.95
-6  -29    9    3114.73     113.32
-6  -28    9    2274.15     122.46
-6  -27    9    3054.75     153.66
-5  -25    9   10072.40     347.53
-5  -24    9      21.41      82.90
-5  -23    9    2840.87     147.18
-4  -21    9    8769.88     167.92
-3  -19    9   22220.07     527.60
-3  -18    9    9399.78     236.70
-2  -17    9   45937.60    1123.98
-2  -16    9   25754.79     636.11
-1  -15    9   30170.37     760.21
0  -13    9  123054.74    3242.71
3   -9    9    3974.05     100.43
4   -8    9   16856.39     348.46
5   -7    9   25135.68     490.82
6   -6    9   43334.47     989.78
10   -3    9  123212.76    3159.17
-5  -29   10    4315.61     128.88
-5  -28   10    1726.07     102.12
-4  -26   10    6544.25     247.15
-4  -25   10   13650.47     250.89
-4  -24   10    2347.72     108.86
-3  -22   10    2519.72     105.27
-3  -21   10    8683.50     211.40
-2  -19   10   25358.32     481.77
-1  -17   10    2064.25      84.74
1  -14   10   10950.02     289.02
2  -12   10    5951.72     155.93
3  -11   10   23411.95     473.71
4  -10   10    5311.58     140.86
8   -6   10   88529.80    1989.82
9   -5   10   10056.09     261.84
12   -3   10   19707.55     500.60
14   -2   10   18618.26     455.01
16   -1   10    3287.40      85.81
-4  -29   11    1510.99     103.12
-3  -27   11    5299.80     206.12
-3  -26   11    1834.99     107.56
-3  -25   11    1481.09      97.66
-2  -23   11    2743.33     123.08
-2  -22   11    7495.53     188.42
-1  -20   11   22867.17     378.77
0  -18   11    6020.07     171.74
1  -16   11    7068.14     120.91
2  -14   11    3719.86     121.52
3  -13   11   90718.81    1868.99
4  -12   11   13158.37     337.41
10   -6   11   44416.57    1081.92
13   -4   11    9716.41     249.87
15   -3   11   67881.05    1621.92
17   -2   11    6330.99     153.66
20   -1   11   13060.50     496.40
-2  -29   12    7859.32     307.17
-2  -28   12    8864.84     313.73
-2  -27   12    3669.69     111.47
-2  -26   12    7544.63     266.59
-1  -24   12    7230.59     260.06
-1  -23   12   10417.21     190.39
0  -21   12    9309.22     144.78
0  -20   12    1266.99      75.51
1  -19   12    4126.83     113.68
1  -18   12    8854.67     225.77
2  -17   12     416.60      52.04
3  -15   12    9905.78     137.74
4  -14   12   14220.16     344.75
6  -11   12   41829.95    1011.89
7  -10   12   10891.20     269.84
11   -7   12   13248.98     455.13
12   -6   12   33729.31     830.41
14   -5   12    1932.76      58.40
16   -4   12   28892.61     676.37
18   -3   12       0.00      23.04
21   -2   12    3336.11     130.43
-1  -28   13    4243.93     116.75
-1  -27   13    3821.34     164.32
0  -26   13   16946.78     586.13
0  -25   13    3694.86     113.03
0  -24   13    8374.51     154.57
1  -22   13    4149.50      95.22
1  -21   13    1486.28     102.24
2  -20   13    4488.65     119.00
2  -19   13      17.60      59.24
3  -18   13   10010.91     233.89
4  -16   13   60027.95     957.64
5  -15   13   15602.66     365.67
6  -13   13   28328.00     684.55
7  -12   13   18042.18     430.75
8  -11   13   28643.04     676.57
9  -10   13    8069.38     270.19
12   -8   13   49561.46    1647.67
13   -7   13    3184.83     115.58
15   -6   13    3118.75     106.46
17   -5   13    9209.64     213.92
23   -3   13    4611.66     177.73
24   -3   13    1772.72      92.99
1  -28   14   15806.80     568.17
1  -27   14    1793.55     105.37
1  -26   14    4303.61     170.35
2  -24   14    7542.47     273.11
2  -23   14    1407.58      86.81
3  -21   14   11680.68     155.26
3  -20   14     480.24     105.66
4  -19   14    2318.34      81.75
5  -17   14    5936.84     123.81
6  -16   14   29007.27     656.33
7  -15   14   28358.31     664.80
8  -13   14   14102.05     337.04
9  -12   14    4146.67     148.46
10  -11   14    2161.04     118.46
13   -9   14   25068.89     830.02
16   -7   14   10893.10     350.76
18   -6   14     893.70      67.85
21   -5   14    6308.09     244.55
22   -5   14   17275.59     652.98
2  -27   15    3301.52     148.55
3  -26   15   11681.77     403.69
3  -25   15    2496.01     119.76
3  -24   15    1561.01     104.37
4  -23   15    4819.01     179.03
4  -22   15   12299.67     178.14
5  -21   15    7146.37     244.26
5  -20   15    8173.27     166.43
6  -19   15    1854.10      71.17
6  -18   15   13059.47     297.55
7  -17   15   23356.07     327.24
8  -16   15    1190.83      55.43
9  -15   15    1931.02     102.93
12  -12   15   24396.25     800.70
13  -11   15   10132.91     341.35
14  -10   15   33487.66    1105.00
16   -9   15   11553.35     367.22
18   -8   15   14677.53     448.24
20   -7   15    1028.24      90.31
21   -7   15   47944.62    2154.63
24   -6   15    2007.02     113.13
25   -6   15    3221.95     156.60
26   -6   15    2927.51     155.26
4  -27   16    1404.09     104.30
4  -26   16    1688.67     104.12
5  -25   16    1187.35      93.59
5  -24   16     441.68     106.73
5  -23   16   18041.88     591.98
6  -23   16    2667.40     167.75
6  -22   16   16770.25     223.13
6  -21   16     463.90     121.10
7  -21   16    1011.96     142.78
7  -20   16   12261.27     182.63
8  -19   16   15232.59     476.91
8  -18   16   17029.49     371.33
9  -17   16    2832.08      95.33
10  -16   16    2828.85      87.98
11  -15   16   18286.07     253.17
12  -14   16    6065.76     133.53
13  -13   16    2580.47      73.75
14  -12   16    2185.09      89.35
16  -11   16    4256.92     140.17
18  -10   16    5292.11     172.59
20   -9   16    9145.53     403.52
23   -8   16    6767.18     295.33
24   -8   16    3602.40     171.20
6  -26   17    1459.92      92.15
6  -25   17    1518.49     146.47
7  -25   17    1648.64     103.14
7  -24   17     156.77      98.31
7  -23   17    2341.84     131.01
8  -23   17    9070.00     307.78
8  -22   17    4473.49     130.05
8  -21   17     747.31     137.03
9  -21   17    7632.26     358.89
9  -20   17    1421.43     106.28
10  -19   17     340.14      91.24
11  -18   17   13991.74     606.79
11  -17   17   17580.06     539.38
12  -17   17   15388.32     475.09
12  -16   17    4948.92     176.85
13  -16   17    1406.34      97.75
13  -15   17    2178.84     122.72
14  -15   17   14658.34     457.26
15  -14   17    2293.12      88.41
16  -13   17    8088.51     245.73
18  -12   17   10814.85     323.79
20  -11   17    5060.37     231.34
21  -11   17    3455.10     202.94
22  -10   17    4068.57     229.98
23  -10   17    1526.04      98.53
24  -10   17   10868.62     493.96
9  -25   18    8472.21     273.90
9  -24   18    1115.52     102.40
10  -23   18    3833.77     197.21
10  -22   18    1353.28     120.44
11  -21   18    3806.06     122.71
11  -20   18   10456.38     510.63
12  -20   18   17044.32     761.65
12  -19   18    3346.91     190.33
13  -19   18   26331.31    1170.88
13  -18   18    1001.63     114.08
14  -18   18    9001.03     432.17
14  -17   18   35271.21    1025.02
15  -17   18    7770.89     368.56
15  -16   18     743.13      86.06
16  -16   18    1422.42      83.02
17  -15   18    7706.33     158.35
18  -14   18    2694.35     108.33
19  -14   18    6446.45     284.83
20  -13   18    7465.32     325.08
21  -13   18     631.00      77.64
23  -12   18    1534.68      98.20
24  -12   18    3083.43     149.10
25  -12   18      94.73      74.23
11  -25   19    1936.04     103.08
11  -24   19     886.95     140.85
12  -24   19    5998.59     304.00
12  -23   19    1281.81     100.24
13  -23   19    5370.88     292.12
13  -22   19    1932.35     104.01
13  -21   19    5360.15     293.48
14  -21   19    2469.22     145.50
14  -20   19    6705.13     313.63
15  -20   19    4235.06     209.87
15  -19   19    4179.25     209.03
16  -19   19    1678.72     118.04
16  -18   19    4933.96     248.45
17  -18   19    2337.34     128.91
18  -17   19    4616.95     128.11
19  -17   19    2739.67     263.74
19  -16   19    2940.28     163.68
20  -16   19    1109.89      89.64
21  -15   19    1540.10     110.27
22  -15   19     306.48      67.90
23  -15   19     430.20      87.61
24  -14   19    1065.12      92.12
25  -14   19    1840.56     103.34
14  -24   20     427.85     100.87
15  -24   20    4384.36     219.32
15  -23   20     203.97      85.73
16  -23   20     535.00      99.42
16  -22   20    2851.25     126.30
17  -22   20    3708.19     194.03
17  -21   20    2158.41     115.89
18  -21   20     483.10     102.42
18  -20   20    1666.20     111.93
19  -20   20     674.70     124.61
19  -19   20    1975.08     161.48
20  -19   20    1574.14     125.48
21  -19   20    6088.80     370.84
21  -18   20    5153.86     298.78
22  -18   20    3618.90     218.06
23  -18   20    2767.30     208.88
23  -17   20    3330.29     211.27
24  -17   20    2860.56     186.51
25  -17   20    2052.05     143.13
19  -23   21    1546.77     133.44
20  -23   21    2536.51     186.60
21  -23   21    3651.67     275.13
20  -22   21     587.09     130.17
21  -22   21    3235.75     129.14
22  -22   21     736.50     129.08
21  -21   21     775.24     156.60
22  -21   21    1224.66     117.90
23  -21   21     957.49     116.78
24  -21   21    4416.14     292.10
25  -21   21    1768.29     200.30
23  -20   21    1240.13     183.23
24  -20   21    1072.46     114.98
25  -20   21    1040.66     113.33
</value>
            </bestfileHKL>
            <bestfilePar>
                <value># parameter file for BEST 
TITLE          .
DETECTOR       ADSC
SITE           Not set
DIAMETER         209.72
PIXEL          0.1024000
ROTAXIS        0.00 0.00 1.00 FAST
POLAXIS        0.00 0.00 1.00
GAIN               0.25
CMOSAIC            0.61
PHISTART           0.00
PHIWIDTH           1.00
DISTANCE         198.37
WAVELENGTH      0.93400
POLARISATION    0.95000
SYMMETRY       P222
UB             -0.008264  0.001266 -0.014851
            0.008851  0.012520 -0.003858
            0.009369 -0.008452 -0.005935
CELL              54.80    59.07    66.98  90.00  90.00  90.00
RASTER           19  17  13   6   5
SEPARATION      0.710  0.710
BEAM            102.520  104.906
# end of parameter file for BEST
</value>
            </bestfilePar>
            <experimentalConditionRefined>
                <beam>
                    <exposureTime>
                        <value>1.000000e+00</value>
                    </exposureTime>
                    <wavelength>
                        <value>9.340000e-01</value>
                    </wavelength>
                </beam>
                <detector>
                    <beamPositionX>
                        <value>1.025197e+02</value>
                    </beamPositionX>
                    <beamPositionY>
                        <value>1.049059e+02</value>
                    </beamPositionY>
                    <bin>
                        <value>2x2</value>
                    </bin>
                    <byteOrder>
                        <value>little_endian</value>
                    </byteOrder>
                    <dataType>
                        <value>unsigned_short</value>
                    </dataType>
                    <distance>
                        <value>1.983700e+02</value>
                    </distance>
                    <imageSaturation>
                        <value>65535</value>
                    </imageSaturation>
                    <name>
                        <value>ADSC Q210 bin 2x2</value>
                    </name>
                    <numberBytesInHeader>
                        <value>512</value>
                    </numberBytesInHeader>
                    <numberPixelX>
                        <value>2048</value>
                    </numberPixelX>
                    <numberPixelY>
                        <value>2048</value>
                    </numberPixelY>
                    <pixelSizeX>
                        <value>1.024000e-01</value>
                    </pixelSizeX>
                    <pixelSizeY>
                        <value>1.024000e-01</value>
                    </pixelSizeY>
                    <serialNumber>
                        <value>444</value>
                    </serialNumber>
                    <twoTheta>
                        <value>0.000000e+00</value>
                    </twoTheta>
                    <type>
                        <value>q210-2x</value>
                    </type>
                </detector>
                <goniostat>
                    <oscillationWidth>
                        <value>1.000000e+00</value>
                    </oscillationWidth>
                    <rotationAxis>
                        <value>phi</value>
                    </rotationAxis>
                    <rotationAxisEnd>
                        <value>9.100000e+01</value>
                    </rotationAxisEnd>
                    <rotationAxisStart>
                        <value>9.000000e+01</value>
                    </rotationAxisStart>
                </goniostat>
            </experimentalConditionRefined>
            <generatedMTZFile>
                <path>
                    <value>/users/svensson/dawb_workspace/workflows-id14eh4/edna-working-dir/ControlCharForReorientationv2_0-00000083/MXv1Characterisation/Integration/MOSFLMIntegrationv10-02/process_1_1.mtz</value>
                </path>
            </generatedMTZFile>
            <statistics>
                <RMSSpotDeviation>
                    <value>6.957900e-02</value>
                </RMSSpotDeviation>
                <iOverSigmaAtHighestResolution>
                    <value>9.182203e+00</value>
                </iOverSigmaAtHighestResolution>
                <iOverSigmaOverall>
                    <value>3.800340e+01</value>
                </iOverSigmaOverall>
                <numberOfBadReflections>
                    <value>6</value>
                </numberOfBadReflections>
                <numberOfFullyRecordedReflections>
                    <value>183</value>
                </numberOfFullyRecordedReflections>
                <numberOfNegativeReflections>
                    <value>89</value>
                </numberOfNegativeReflections>
                <numberOfOverlappedReflections>
                    <value>1</value>
                </numberOfOverlappedReflections>
                <numberOfPartialReflections>
                    <value>1511</value>
                </numberOfPartialReflections>
            </statistics>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>4.149451e+00</value>
                </maxResolution>
                <minResolution>
                    <value>4.149451e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>4.780652e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.119340e+05</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.314000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>17</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>3.767996e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.573770e+05</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.834000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>114</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>3.821030e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.112590e+05</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.801000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>17</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>3.645007e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.530030e+05</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.834000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>114</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>2.934117e+00</value>
                </maxResolution>
                <minResolution>
                    <value>4.149451e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>6.190391e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.359470e+05</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.287000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>26</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>3.282412e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>6.188300e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>1.611000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>213</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>3.642824e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.301560e+05</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.399000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>26</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>3.091239e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>5.880800e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>1.611000e+03</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>213</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>2.395700e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.934117e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>4.392500e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>3.446000e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>6.410000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>34</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>2.680253e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>2.362000e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>6.770000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>275</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>2.917018e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>3.100500e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>9.290000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>34</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>2.435835e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>2.136900e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>6.770000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>275</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>2.074739e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.395700e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>3.743663e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.842900e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.940000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>44</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>1.844350e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.279400e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>5.450000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>309</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>2.150500e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.740800e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>6.710000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>44</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>1.776523e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.242100e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>5.450000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>309</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>1.855704e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.074739e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>2.541178e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.188000e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.520000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>40</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>1.376633e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>7.497000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>4.050000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>311</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>1.875770e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.161200e+04</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>5.000000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>40</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>1.407109e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>7.637000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>4.050000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>311</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>1.694018e+00</value>
                </maxResolution>
                <minResolution>
                    <value>1.855704e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>1.800736e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>5.806000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.570000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>14</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>9.547879e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>2.882000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.450000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>178</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>1.420535e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>6.136000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>3.530000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>14</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>1.035191e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>3.104000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.450000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>178</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>1.568357e+00</value>
                </maxResolution>
                <minResolution>
                    <value>1.694018e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>1.266470e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>5.398000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.940000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>6</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>6.003360e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.554000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.140000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>88</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>1.163696e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>7.367000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>4.210000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>6</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>6.919854e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.783000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.140000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>88</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <statisticsPerResolutionBin>
                <maxResolution>
                    <value>1.467063e+00</value>
                </maxResolution>
                <minResolution>
                    <value>1.568357e+00</value>
                </minResolution>
                <profileFitted>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>9.182203e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>2.167000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.360000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>1</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>3.706289e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>9.300000e+02</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>1.930000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>19</value>
                        </numberOfReflections>
                    </partials>
                </profileFitted>
                <summation>
                    <fullyRecorded>
                        <averageIOverSigma>
                            <value>1.221923e+01</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>3.177000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>2.600000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>1</value>
                        </numberOfReflections>
                    </fullyRecorded>
                    <partials>
                        <averageIOverSigma>
                            <value>4.578049e+00</value>
                        </averageIOverSigma>
                        <averageIntensity>
                            <value>1.115000e+03</value>
                        </averageIntensity>
                        <averageSigma>
                            <value>1.930000e+02</value>
                        </averageSigma>
                        <numberOfReflections>
                            <value>19</value>
                        </numberOfReflections>
                    </partials>
                </summation>
            </statisticsPerResolutionBin>
            <subWedgeNumber>
                <value>1</value>
            </subWedgeNumber>
        </integrationSubWedgeResult>
    </integrationResult>
    <shortSummary>
        <value>ImageQualityIndicators: ref-testscale_1_0002.img: good bragg 1224, r1 1.9 [A], r2 1.8 [A], max cell 208.2 [A], ice rings 0, total integrated signal 10896280
ImageQualityIndicators: ref-testscale_1_0001.img: good bragg 1042, r1 1.9 [A], r2 1.9 [A], max cell 206.4 [A], ice rings 0, total integrated signal 10416170
Indexing: laue/space group P222, mosaicity 0.58 [degree], RMS dev pos 0.15 [mm] ang 0.44 [degree]
Indexing: refined Cell:   54.80   59.07   66.98   90.00   90.00   90.00
Integration: 0 no full: 200, part: 1511, bad/neg/ovrlp: 45, RMS dev: 0.063 [mm], I/sigma overall 45.5 at highest res 6.4
Integration: 1 no full: 183, part: 1511, bad/neg/ovrlp: 96, RMS dev: 0.070 [mm], I/sigma overall 38.0 at highest res 9.2
</value>
    </shortSummary>
    <statusMessage>
        <value>MOSFLM: Indexing successful (P222). Integration successful.</value>
    </statusMessage>
    <strategyResult>
        <bestLogFile>
            <path>
                <value>/users/svensson/dawb_workspace/workflows-id14eh4/edna-working-dir/ControlCharForReorientationv2_0-00000083/MXv2KappaStrategy/ControlStrategyv1_2/Bestv1_2/best.log</value>
            </path>
        </bestLogFile>
        <collectionPlan>
            <collectionPlanNumber>
                <value>1</value>
            </collectionPlanNumber>
            <collectionStrategy>
                <sample>
                    <crystal>
                        <cell>
                            <angle_alpha>
                                <value>9.000000e+01</value>
                            </angle_alpha>
                            <angle_beta>
                                <value>9.000000e+01</value>
                            </angle_beta>
                            <angle_gamma>
                                <value>9.000000e+01</value>
                            </angle_gamma>
                            <length_a>
                                <value>5.480450e+01</value>
                            </length_a>
                            <length_b>
                                <value>5.907400e+01</value>
                            </length_b>
                            <length_c>
                                <value>6.698280e+01</value>
                            </length_c>
                        </cell>
                        <mosaicity>
                            <value>5.850000e-01</value>
                        </mosaicity>
                        <spaceGroup>
                            <ITNumber>
                                <value>16</value>
                            </ITNumber>
                            <name>
                                <value>P222</value>
                            </name>
                        </spaceGroup>
                    </crystal>
                    <chemicalComposition>
                        <solvent>
                            <atoms>
                                <atom>
                                    <concentration>
                                        <value>3.140000e+02</value>
                                    </concentration>
                                    <symbol>
                                        <value>S</value>
                                    </symbol>
                                </atom>
                            </atoms>
                        </solvent>
                        <structure>
                            <chain>
                                <heavyAtoms>
                                    <atom>
                                        <numberOf>
                                            <value>1.100000e+01</value>
                                        </numberOf>
                                        <symbol>
                                            <value>S</value>
                                        </symbol>
                                    </atom>
                                </heavyAtoms>
                                <numberOfCopies>
                                    <value>1.000000e+00</value>
                                </numberOfCopies>
                                <numberOfMonomers>
                                    <value>2.120000e+02</value>
                                </numberOfMonomers>
                                <type>
                                    <value>protein</value>
                                </type>
                            </chain>
                            <numberOfCopiesInAsymmetricUnit>
                                <value>1.000000e+00</value>
                            </numberOfCopiesInAsymmetricUnit>
                        </structure>
                    </chemicalComposition>
                </sample>
                <subWedge>
                    <experimentalCondition>
                        <beam>
                            <exposureTime>
                                <value>3.700000e-02</value>
                            </exposureTime>
                            <transmission>
                                <value>1.000000e+02</value>
                            </transmission>
                            <wavelength>
                                <value>9.340000e-01</value>
                            </wavelength>
                        </beam>
                        <detector>
                            <beamPositionX>
                                <value>1.025087e+02</value>
                            </beamPositionX>
                            <beamPositionY>
                                <value>1.048387e+02</value>
                            </beamPositionY>
                            <bin>
                                <value>2x2</value>
                            </bin>
                            <byteOrder>
                                <value>little_endian</value>
                            </byteOrder>
                            <dataType>
                                <value>unsigned_short</value>
                            </dataType>
                            <distance>
                                <value>2.032700e+02</value>
                            </distance>
                            <imageSaturation>
                                <value>65535</value>
                            </imageSaturation>
                            <name>
                                <value>ADSC Q210 bin 2x2</value>
                            </name>
                            <numberBytesInHeader>
                                <value>512</value>
                            </numberBytesInHeader>
                            <numberPixelX>
                                <value>2048</value>
                            </numberPixelX>
                            <numberPixelY>
                                <value>2048</value>
                            </numberPixelY>
                            <pixelSizeX>
                                <value>1.024000e-01</value>
                            </pixelSizeX>
                            <pixelSizeY>
                                <value>1.024000e-01</value>
                            </pixelSizeY>
                            <serialNumber>
                                <value>444</value>
                            </serialNumber>
                            <twoTheta>
                                <value>0.000000e+00</value>
                            </twoTheta>
                            <type>
                                <value>q210-2x</value>
                            </type>
                        </detector>
                        <goniostat>
                            <oscillationWidth>
                                <value>1.750000e+00</value>
                            </oscillationWidth>
                            <rotationAxis>
                                <value>phi</value>
                            </rotationAxis>
                            <rotationAxisEnd>
                                <value>2.135000e+02</value>
                            </rotationAxisEnd>
                            <rotationAxisStart>
                                <value>1.050000e+02</value>
                            </rotationAxisStart>
                        </goniostat>
                    </experimentalCondition>
                    <subWedgeNumber>
                        <value>1</value>
                    </subWedgeNumber>
                </subWedge>
            </collectionStrategy>
            <statistics>
                <resolutionBin>
                    <IOverSigma>
                        <value>4.280000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>7.199140e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>4.010000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>1.797400e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>9.900000e-01</value>
                    </completeness>
                    <maxResolution>
                        <value>7.730000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>1.200000e+01</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>3.200000e+00</value>
                    </rFactor>
                    <redundancy>
                        <value>3.940000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>2.840000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>4.223230e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>2.590000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>1.629700e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>6.140000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>7.730000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>5.200000e+00</value>
                    </rFactor>
                    <redundancy>
                        <value>4.070000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>2.540000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>4.224850e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>2.310000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>1.825100e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>5.250000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>6.140000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>5.900000e+00</value>
                    </rFactor>
                    <redundancy>
                        <value>4.140000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>3.100000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>6.491450e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>2.870000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.265700e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>4.660000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>5.250000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>4.800000e+00</value>
                    </rFactor>
                    <redundancy>
                        <value>4.200000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>3.340000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>8.134780e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>3.110000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.612100e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>4.230000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>4.660000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>4.500000e+00</value>
                    </rFactor>
                    <redundancy>
                        <value>4.380000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>3.050000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>7.639090e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>2.820000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.705700e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>3.900000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>4.230000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>4.900000e+00</value>
                    </rFactor>
                    <redundancy>
                        <value>4.300000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>2.720000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>6.861950e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>2.510000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.730700e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>3.640000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>3.900000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>5.700000e+00</value>
                    </rFactor>
                    <redundancy>
                        <value>4.390000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>2.350000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>5.993640e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>2.170000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.764800e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>3.430000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>3.640000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>6.600000e+00</value>
                    </rFactor>
                    <redundancy>
                        <value>4.380000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>1.990000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>5.011010e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>1.820000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.754700e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>3.240000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>3.430000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>7.900000e+00</value>
                    </rFactor>
                    <redundancy>
                        <value>4.450000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>1.620000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>4.025610e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>1.480000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.718000e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>3.090000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>3.240000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>9.900000e+00</value>
                    </rFactor>
                    <redundancy>
                        <value>4.480000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>1.350000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>3.358240e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>1.220000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.746500e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.950000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>3.090000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>1.200000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.410000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>1.120000e+01</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>2.812890e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>1.010000e+01</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.794000e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.840000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.950000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>1.460000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.410000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>9.400000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>2.420600e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>8.500000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.858600e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.730000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.840000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>1.740000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.450000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>8.400000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>2.176190e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>7.500000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.888200e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.640000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.730000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>1.970000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.450000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>7.500000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>2.010220e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>6.800000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>2.973300e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.550000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.640000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>2.180000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.360000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>6.700000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>1.853320e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>6.100000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>3.046700e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.470000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.550000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>2.450000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.410000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>6.200000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>1.758020e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>5.600000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>3.131500e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.400000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.470000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>2.640000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.360000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>5.800000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>1.691760e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>5.300000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>3.203700e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.340000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.400000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>2.810000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.380000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>5.500000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>1.634240e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>5.000000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>3.291900e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.280000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.340000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>3.000000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.380000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>5.200000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>1.578010e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>4.700000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>3.358100e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.220000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.280000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>3.170000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.350000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>4.800000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>1.502090e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>4.400000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>3.446700e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.170000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.220000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>3.420000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.360000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>4.400000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>1.406760e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>4.000000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>3.500600e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.120000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.170000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>3.750000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.510000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>4.000000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>1.330560e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>3.700000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>3.617300e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.080000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.120000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>4.020000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.490000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>3.600000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>1.205090e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>3.300000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>3.676000e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>2.030000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.080000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>4.550000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.480000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>3.100000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>1.087570e+02</value>
                    </averageIntensity>
                    <averageIntensityOverAverageSigma>
                        <value>2.900000e+00</value>
                    </averageIntensityOverAverageSigma>
                    <averageSigma>
                        <value>3.793700e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>1.990000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>2.030000e+00</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>5.110000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.500000e+00</value>
                    </redundancy>
                </resolutionBin>
                <resolutionBin>
                    <IOverSigma>
                        <value>9.600000e+00</value>
                    </IOverSigma>
                    <averageIntensity>
                        <value>2.885200e+02</value>
                    </averageIntensity>
                    <averageSigma>
                        <value>3.004700e+01</value>
                    </averageSigma>
                    <completeness>
                        <value>1.000000e+00</value>
                    </completeness>
                    <maxResolution>
                        <value>1.990000e+00</value>
                    </maxResolution>
                    <minResolution>
                        <value>1.200000e+01</value>
                    </minResolution>
                    <percentageOverload>
                        <value>0.000000e+00</value>
                    </percentageOverload>
                    <rFactor>
                        <value>1.550000e+01</value>
                    </rFactor>
                    <redundancy>
                        <value>4.390000e+00</value>
                    </redundancy>
                </resolutionBin>
            </statistics>
            <strategySummary>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <iSigma>
                    <value>2.800000e+00</value>
                </iSigma>
                <rankingResolution>
                    <value>1.210000e+00</value>
                </rankingResolution>
                <redundancy>
                    <value>4.390000e+00</value>
                </redundancy>
                <resolution>
                    <value>1.990000e+00</value>
                </resolution>
                <resolutionReasoning>
                    <value>Resolution limit is set by the initial image resolution</value>
                </resolutionReasoning>
                <totalDataCollectionTime>
                    <value>1.573150e+02</value>
                </totalDataCollectionTime>
                <totalExposureTime>
                    <value>2.315000e+00</value>
                </totalExposureTime>
            </strategySummary>
        </collectionPlan>
    </strategyResult>
</mxv1ResultCharacterisation_Reference>
"""


possibleOrientations = """
<possibleOrientations>
    <status>
        <code>
        </code>
    </status>
    <comment>Calculation performed by STAC (using gonset from Phil Evans)</comment>
    <possible_orientation>
        <v1>(1.0;0.0;0.0)</v1>
        <v2>(0.0;1.0;0.0)</v2>
        <omega>2.000150e+02</omega>
        <kappa>2.860530e+02</kappa>
        <phi>1.777380e+02</phi>
        <trans>(0.0001;-0.6960;0.5353)</trans>
        <rank>1.686873e+03</rank>
    </possible_orientation>
    <possible_orientation>
        <v1>(1.0;0.0;0.0)</v1>
        <v2>(0.0;1.0;0.0)</v2>
        <omega>2.001500e+01</omega>
        <kappa>2.860530e+02</kappa>
        <phi>1.777380e+02</phi>
        <trans>(0.0001;-0.6960;0.5353)</trans>
        <rank>1.686876e+03</rank>
    </possible_orientation>
    <possible_orientation>
        <v1>(1.0;0.0;0.0)</v1>
        <v2>(0.0;0.0;1.0)</v2>
        <omega>1.100140e+02</omega>
        <kappa>2.860530e+02</kappa>
        <phi>1.777380e+02</phi>
        <trans>(0.0001;-0.6960;0.5353)</trans>
        <rank>1.765938e+03</rank>
    </possible_orientation>
    <possible_orientation>
        <v1>(1.0;0.0;0.0)</v1>
        <v2>(0.0;0.0;1.0)</v2>
        <omega>2.900140e+02</omega>
        <kappa>2.860530e+02</kappa>
        <phi>1.777380e+02</phi>
        <trans>(0.0001;-0.6960;0.5353)</trans>
        <rank>1.765884e+03</rank>
    </possible_orientation>
    </possibleOrientations>
"""


suggestedStrategy = """
<XSDataResultStrategy>
    <bestLogFile>
        <path>
            <value>/users/svensson/dawb_workspace/workflows-id14eh4/edna-working-dir/ControlCharForReorientationv2_0-00000083/MXv2KappaStrategy/ControlStrategyv1_2/Bestv1_2/best.log</value>
        </path>
    </bestLogFile>
    <collectionPlan>
        <collectionPlanNumber>
            <value>1</value>
        </collectionPlanNumber>
        <collectionStrategy>
            <diffractionPlan>
                <complexity>
                    <value>full</value>
                </complexity>
                <kappaStrategyOption>
                    <value>Cell</value>
                </kappaStrategyOption>
                <maxExposureTimePerDataCollection>
                    <value>1.000000e+03</value>
                </maxExposureTimePerDataCollection>
            </diffractionPlan>
            <subWedge>
                <experimentalCondition>
                    <beam>
                        <exposureTime>
                            <value>1.000000e+00</value>
                        </exposureTime>
                        <wavelength>
                            <value>9.340000e-01</value>
                        </wavelength>
                    </beam>
                    <detector>
                        <beamPositionX>
                            <value>1.024590e+02</value>
                        </beamPositionX>
                        <beamPositionY>
                            <value>1.047380e+02</value>
                        </beamPositionY>
                        <bin>
                            <value>2x2</value>
                        </bin>
                        <byteOrder>
                            <value>little_endian</value>
                        </byteOrder>
                        <dataType>
                            <value>unsigned_short</value>
                        </dataType>
                        <distance>
                            <value>1.984410e+02</value>
                        </distance>
                        <imageSaturation>
                            <value>65535</value>
                        </imageSaturation>
                        <name>
                            <value>ADSC Q210 bin 2x2</value>
                        </name>
                        <numberBytesInHeader>
                            <value>512</value>
                        </numberBytesInHeader>
                        <numberPixelX>
                            <value>2048</value>
                        </numberPixelX>
                        <numberPixelY>
                            <value>2048</value>
                        </numberPixelY>
                        <pixelSizeX>
                            <value>1.024000e-01</value>
                        </pixelSizeX>
                        <pixelSizeY>
                            <value>1.024000e-01</value>
                        </pixelSizeY>
                        <serialNumber>
                            <value>444</value>
                        </serialNumber>
                        <twoTheta>
                            <value>0.000000e+00</value>
                        </twoTheta>
                        <type>
                            <value>q210-2x</value>
                        </type>
                    </detector>
                    <goniostat>
                        <oscillationWidth>
                            <value>1.000000e+00</value>
                        </oscillationWidth>
                        <rotationAxis>
                            <value>phi</value>
                        </rotationAxis>
                        <rotationAxisEnd>
                            <value>9.100000e+01</value>
                        </rotationAxisEnd>
                        <rotationAxisStart>
                            <value>9.000000e+01</value>
                        </rotationAxisStart>
                    </goniostat>
                </experimentalCondition>
                <image>
                    <date>
                        <value>Mon Mar 20 12:38:28 2006</value>
                    </date>
                    <number>
                        <value>2</value>
                    </number>
                    <path>
                        <value>/opt/pxsoft/DNA/TestCase/RAW_DATA/ref-testscale_1_0002.img</value>
                    </path>
                </image>
            </subWedge>
            <subWedge>
                <experimentalCondition>
                    <beam>
                        <exposureTime>
                            <value>1.000000e+00</value>
                        </exposureTime>
                        <wavelength>
                            <value>9.340000e-01</value>
                        </wavelength>
                    </beam>
                    <detector>
                        <beamPositionX>
                            <value>1.024590e+02</value>
                        </beamPositionX>
                        <beamPositionY>
                            <value>1.047380e+02</value>
                        </beamPositionY>
                        <bin>
                            <value>2x2</value>
                        </bin>
                        <byteOrder>
                            <value>little_endian</value>
                        </byteOrder>
                        <dataType>
                            <value>unsigned_short</value>
                        </dataType>
                        <distance>
                            <value>1.984410e+02</value>
                        </distance>
                        <imageSaturation>
                            <value>65535</value>
                        </imageSaturation>
                        <name>
                            <value>ADSC Q210 bin 2x2</value>
                        </name>
                        <numberBytesInHeader>
                            <value>512</value>
                        </numberBytesInHeader>
                        <numberPixelX>
                            <value>2048</value>
                        </numberPixelX>
                        <numberPixelY>
                            <value>2048</value>
                        </numberPixelY>
                        <pixelSizeX>
                            <value>1.024000e-01</value>
                        </pixelSizeX>
                        <pixelSizeY>
                            <value>1.024000e-01</value>
                        </pixelSizeY>
                        <serialNumber>
                            <value>444</value>
                        </serialNumber>
                        <twoTheta>
                            <value>0.000000e+00</value>
                        </twoTheta>
                        <type>
                            <value>q210-2x</value>
                        </type>
                    </detector>
                    <goniostat>
                        <oscillationWidth>
                            <value>1.000000e+00</value>
                        </oscillationWidth>
                        <rotationAxis>
                            <value>phi</value>
                        </rotationAxis>
                        <rotationAxisEnd>
                            <value>1.000000e+00</value>
                        </rotationAxisEnd>
                        <rotationAxisStart>
                            <value>0.000000e+00</value>
                        </rotationAxisStart>
                    </goniostat>
                </experimentalCondition>
                <image>
                    <date>
                        <value>Mon Mar 20 12:38:23 2006</value>
                    </date>
                    <number>
                        <value>1</value>
                    </number>
                    <path>
                        <value>/opt/pxsoft/DNA/TestCase/RAW_DATA/ref-testscale_1_0001.img</value>
                    </path>
                </image>
            </subWedge>
        </collectionStrategy>
        <comment>
            <value>OMEGA=309.219 KAPPA=76.906 PHI=287.658</value>
        </comment>
        <statistics>
            <resolutionBin>
                <IOverSigma>
                    <value>4.280000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>7.199140e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>4.010000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>1.797400e+01</value>
                </averageSigma>
                <completeness>
                    <value>9.900000e-01</value>
                </completeness>
                <maxResolution>
                    <value>7.730000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>1.200000e+01</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>3.200000e+00</value>
                </rFactor>
                <redundancy>
                    <value>3.940000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>2.840000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>4.223230e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.590000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>1.629700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>6.140000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>7.730000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>5.200000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.070000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>2.540000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>4.224850e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.310000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>1.825100e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>5.250000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>6.140000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>5.900000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.140000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>3.100000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>6.491450e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.870000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.265700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>4.660000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>5.250000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>4.800000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.200000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>3.340000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>8.134780e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>3.110000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.612100e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>4.230000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>4.660000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>4.500000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.380000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>3.050000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>7.639090e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.820000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.705700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>3.900000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>4.230000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>4.900000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.300000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>2.720000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>6.861950e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.510000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.730700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>3.640000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>3.900000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>5.700000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.390000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>2.350000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>5.993640e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.170000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.764800e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>3.430000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>3.640000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>6.600000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.380000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>1.990000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>5.011010e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>1.820000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.754700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>3.240000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>3.430000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>7.900000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.450000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>1.620000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>4.025610e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>1.480000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.718000e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>3.090000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>3.240000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>9.900000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.480000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>1.350000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>3.358240e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>1.220000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.746500e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.950000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>3.090000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>1.200000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.410000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>1.120000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>2.812890e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>1.010000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.794000e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.840000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.950000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>1.460000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.410000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>9.400000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>2.420600e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>8.500000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.858600e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.730000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.840000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>1.740000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.450000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>8.400000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>2.176190e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>7.500000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.888200e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.640000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.730000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>1.970000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.450000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>7.500000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>2.010220e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>6.800000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.973300e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.550000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.640000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>2.180000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.360000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>6.700000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.853320e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>6.100000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.046700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.470000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.550000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>2.450000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.410000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>6.200000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.758020e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>5.600000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.131500e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.400000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.470000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>2.640000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.360000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>5.800000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.691760e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>5.300000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.203700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.340000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.400000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>2.810000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.380000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>5.500000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.634240e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>5.000000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.291900e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.280000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.340000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>3.000000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.380000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>5.200000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.578010e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>4.700000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.358100e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.220000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.280000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>3.170000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.350000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>4.800000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.502090e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>4.400000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.446700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.170000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.220000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>3.420000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.360000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>4.400000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.406760e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>4.000000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.500600e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.120000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.170000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>3.750000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.510000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>4.000000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.330560e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>3.700000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.617300e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.080000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.120000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>4.020000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.490000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>3.600000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.205090e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>3.300000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.676000e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.030000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.080000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>4.550000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.480000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>3.100000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.087570e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.900000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.793700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>1.990000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.030000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>5.110000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.500000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>9.600000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>2.885200e+02</value>
                </averageIntensity>
                <averageSigma>
                    <value>3.004700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>1.990000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>1.200000e+01</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>1.550000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.390000e+00</value>
                </redundancy>
            </resolutionBin>
        </statistics>
        <strategySummary>
            <completeness>
                <value>1.000000e+00</value>
            </completeness>
            <iSigma>
                <value>2.800000e+00</value>
            </iSigma>
            <rankingResolution>
                <value>1.210000e+00</value>
            </rankingResolution>
            <redundancy>
                <value>4.390000e+00</value>
            </redundancy>
            <resolution>
                <value>1.990000e+00</value>
            </resolution>
            <resolutionReasoning>
                <value>Resolution limit is set by the initial image resolution</value>
            </resolutionReasoning>
            <totalDataCollectionTime>
                <value>1.573150e+02</value>
            </totalDataCollectionTime>
            <totalExposureTime>
                <value>2.315000e+00</value>
            </totalExposureTime>
        </strategySummary>
    </collectionPlan>
</XSDataResultStrategy>
"""



mxv1StrategyResult="""<XSDataResultStrategy>
    <bestLogFile>
        <path>
            <value>/users/svensson/dawb_workspace/workflows-id14eh4/edna-working-dir/ControlCharForReorientationv2_0-00000083/MXv2KappaStrategy/ControlStrategyv1_2/Bestv1_2/best.log</value>
        </path>
    </bestLogFile>
    <collectionPlan>
        <collectionPlanNumber>
            <value>1</value>
        </collectionPlanNumber>
        <collectionStrategy>
            <sample>
                <crystal>
                    <cell>
                        <angle_alpha>
                            <value>9.000000e+01</value>
                        </angle_alpha>
                        <angle_beta>
                            <value>9.000000e+01</value>
                        </angle_beta>
                        <angle_gamma>
                            <value>9.000000e+01</value>
                        </angle_gamma>
                        <length_a>
                            <value>5.480450e+01</value>
                        </length_a>
                        <length_b>
                            <value>5.907400e+01</value>
                        </length_b>
                        <length_c>
                            <value>6.698280e+01</value>
                        </length_c>
                    </cell>
                    <mosaicity>
                        <value>5.850000e-01</value>
                    </mosaicity>
                    <spaceGroup>
                        <ITNumber>
                            <value>16</value>
                        </ITNumber>
                        <name>
                            <value>P222</value>
                        </name>
                    </spaceGroup>
                </crystal>
                <chemicalComposition>
                    <solvent>
                        <atoms>
                            <atom>
                                <concentration>
                                    <value>3.140000e+02</value>
                                </concentration>
                                <symbol>
                                    <value>S</value>
                                </symbol>
                            </atom>
                        </atoms>
                    </solvent>
                    <structure>
                        <chain>
                            <heavyAtoms>
                                <atom>
                                    <numberOf>
                                        <value>1.100000e+01</value>
                                    </numberOf>
                                    <symbol>
                                        <value>S</value>
                                    </symbol>
                                </atom>
                            </heavyAtoms>
                            <numberOfCopies>
                                <value>1.000000e+00</value>
                            </numberOfCopies>
                            <numberOfMonomers>
                                <value>2.120000e+02</value>
                            </numberOfMonomers>
                            <type>
                                <value>protein</value>
                            </type>
                        </chain>
                        <numberOfCopiesInAsymmetricUnit>
                            <value>1.000000e+00</value>
                        </numberOfCopiesInAsymmetricUnit>
                    </structure>
                </chemicalComposition>
            </sample>
            <subWedge>
                <experimentalCondition>
                    <beam>
                        <exposureTime>
                            <value>3.700000e-02</value>
                        </exposureTime>
                        <transmission>
                            <value>1.000000e+02</value>
                        </transmission>
                        <wavelength>
                            <value>9.340000e-01</value>
                        </wavelength>
                    </beam>
                    <detector>
                        <beamPositionX>
                            <value>1.025087e+02</value>
                        </beamPositionX>
                        <beamPositionY>
                            <value>1.048387e+02</value>
                        </beamPositionY>
                        <bin>
                            <value>2x2</value>
                        </bin>
                        <byteOrder>
                            <value>little_endian</value>
                        </byteOrder>
                        <dataType>
                            <value>unsigned_short</value>
                        </dataType>
                        <distance>
                            <value>2.032700e+02</value>
                        </distance>
                        <imageSaturation>
                            <value>65535</value>
                        </imageSaturation>
                        <name>
                            <value>ADSC Q210 bin 2x2</value>
                        </name>
                        <numberBytesInHeader>
                            <value>512</value>
                        </numberBytesInHeader>
                        <numberPixelX>
                            <value>2048</value>
                        </numberPixelX>
                        <numberPixelY>
                            <value>2048</value>
                        </numberPixelY>
                        <pixelSizeX>
                            <value>1.024000e-01</value>
                        </pixelSizeX>
                        <pixelSizeY>
                            <value>1.024000e-01</value>
                        </pixelSizeY>
                        <serialNumber>
                            <value>444</value>
                        </serialNumber>
                        <twoTheta>
                            <value>0.000000e+00</value>
                        </twoTheta>
                        <type>
                            <value>q210-2x</value>
                        </type>
                    </detector>
                    <goniostat>
                        <oscillationWidth>
                            <value>1.750000e+00</value>
                        </oscillationWidth>
                        <rotationAxis>
                            <value>phi</value>
                        </rotationAxis>
                        <rotationAxisEnd>
                            <value>2.135000e+02</value>
                        </rotationAxisEnd>
                        <rotationAxisStart>
                            <value>1.050000e+02</value>
                        </rotationAxisStart>
                    </goniostat>
                </experimentalCondition>
                <subWedgeNumber>
                    <value>1</value>
                </subWedgeNumber>
            </subWedge>
        </collectionStrategy>
        <statistics>
            <resolutionBin>
                <IOverSigma>
                    <value>4.280000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>7.199140e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>4.010000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>1.797400e+01</value>
                </averageSigma>
                <completeness>
                    <value>9.900000e-01</value>
                </completeness>
                <maxResolution>
                    <value>7.730000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>1.200000e+01</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>3.200000e+00</value>
                </rFactor>
                <redundancy>
                    <value>3.940000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>2.840000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>4.223230e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.590000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>1.629700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>6.140000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>7.730000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>5.200000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.070000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>2.540000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>4.224850e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.310000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>1.825100e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>5.250000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>6.140000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>5.900000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.140000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>3.100000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>6.491450e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.870000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.265700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>4.660000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>5.250000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>4.800000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.200000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>3.340000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>8.134780e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>3.110000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.612100e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>4.230000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>4.660000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>4.500000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.380000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>3.050000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>7.639090e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.820000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.705700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>3.900000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>4.230000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>4.900000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.300000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>2.720000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>6.861950e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.510000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.730700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>3.640000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>3.900000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>5.700000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.390000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>2.350000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>5.993640e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.170000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.764800e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>3.430000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>3.640000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>6.600000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.380000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>1.990000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>5.011010e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>1.820000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.754700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>3.240000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>3.430000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>7.900000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.450000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>1.620000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>4.025610e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>1.480000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.718000e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>3.090000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>3.240000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>9.900000e+00</value>
                </rFactor>
                <redundancy>
                    <value>4.480000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>1.350000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>3.358240e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>1.220000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.746500e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.950000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>3.090000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>1.200000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.410000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>1.120000e+01</value>
                </IOverSigma>
                <averageIntensity>
                    <value>2.812890e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>1.010000e+01</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.794000e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.840000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.950000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>1.460000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.410000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>9.400000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>2.420600e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>8.500000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.858600e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.730000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.840000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>1.740000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.450000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>8.400000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>2.176190e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>7.500000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.888200e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.640000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.730000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>1.970000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.450000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>7.500000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>2.010220e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>6.800000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>2.973300e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.550000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.640000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>2.180000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.360000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>6.700000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.853320e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>6.100000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.046700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.470000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.550000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>2.450000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.410000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>6.200000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.758020e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>5.600000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.131500e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.400000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.470000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>2.640000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.360000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>5.800000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.691760e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>5.300000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.203700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.340000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.400000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>2.810000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.380000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>5.500000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.634240e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>5.000000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.291900e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.280000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.340000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>3.000000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.380000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>5.200000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.578010e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>4.700000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.358100e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.220000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.280000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>3.170000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.350000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>4.800000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.502090e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>4.400000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.446700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.170000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.220000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>3.420000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.360000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>4.400000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.406760e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>4.000000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.500600e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.120000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.170000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>3.750000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.510000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>4.000000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.330560e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>3.700000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.617300e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.080000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.120000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>4.020000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.490000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>3.600000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.205090e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>3.300000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.676000e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>2.030000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.080000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>4.550000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.480000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>3.100000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>1.087570e+02</value>
                </averageIntensity>
                <averageIntensityOverAverageSigma>
                    <value>2.900000e+00</value>
                </averageIntensityOverAverageSigma>
                <averageSigma>
                    <value>3.793700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>1.990000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>2.030000e+00</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>5.110000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.500000e+00</value>
                </redundancy>
            </resolutionBin>
            <resolutionBin>
                <IOverSigma>
                    <value>9.600000e+00</value>
                </IOverSigma>
                <averageIntensity>
                    <value>2.885200e+02</value>
                </averageIntensity>
                <averageSigma>
                    <value>3.004700e+01</value>
                </averageSigma>
                <completeness>
                    <value>1.000000e+00</value>
                </completeness>
                <maxResolution>
                    <value>1.990000e+00</value>
                </maxResolution>
                <minResolution>
                    <value>1.200000e+01</value>
                </minResolution>
                <percentageOverload>
                    <value>0.000000e+00</value>
                </percentageOverload>
                <rFactor>
                    <value>1.550000e+01</value>
                </rFactor>
                <redundancy>
                    <value>4.390000e+00</value>
                </redundancy>
            </resolutionBin>
        </statistics>
        <strategySummary>
            <completeness>
                <value>1.000000e+00</value>
            </completeness>
            <iSigma>
                <value>2.800000e+00</value>
            </iSigma>
            <rankingResolution>
                <value>1.210000e+00</value>
            </rankingResolution>
            <redundancy>
                <value>4.390000e+00</value>
            </redundancy>
            <resolution>
                <value>1.990000e+00</value>
            </resolution>
            <resolutionReasoning>
                <value>Resolution limit is set by the initial image resolution</value>
            </resolutionReasoning>
            <totalDataCollectionTime>
                <value>1.573150e+02</value>
            </totalDataCollectionTime>
            <totalExposureTime>
                <value>2.315000e+00</value>
            </totalExposureTime>
        </strategySummary>
    </collectionPlan>
</XSDataResultStrategy>"""
