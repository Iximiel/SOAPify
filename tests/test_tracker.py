from numpy.testing import assert_array_equal
import SOAPify
import numpy
from SOAPify.classify import SOAPclassification


def test_transitionMatrixFromTracking(input_mockedTrajectoryClassification):
    data = input_mockedTrajectoryClassification
    events = SOAPify.trackStates(data)
    for event in events:
        print(event)
    transitionMatrixFromTracking = SOAPify.calculateTransitionMatrix(
        data, stride=1, statesTracker=events
    )
    expectedTmat = SOAPify.transitionMatrixFromSOAPClassification(data, stride=1)
    standardTmat = SOAPify.calculateTransitionMatrix(data, stride=1)
    assert_array_equal(transitionMatrixFromTracking, expectedTmat)
    assert_array_equal(standardTmat, expectedTmat)
    assert isinstance(events[0], list)


def test_stateTracker(input_mockedTrajectoryClassification):
    data: SOAPclassification = input_mockedTrajectoryClassification
    # code for derermining the events
    CURSTATE = SOAPify.TRACK_CURSTATE
    ENDSTATE = SOAPify.TRACK_ENDSTATE
    TIME = SOAPify.TRACK_EVENTTIME
    expectedEvents = []
    for atomID in range(data.references.shape[1]):
        eventsperAtom = []
        atomTraj = data.references[:, atomID]
        # the array is [start state, state, end state,time]
        # wg
        event = numpy.array([atomTraj[0], atomTraj[0], atomTraj[0], 0], dtype=int)
        for frame in range(1, data.references.shape[0]):
            if atomTraj[frame] != event[CURSTATE]:
                event[ENDSTATE] = atomTraj[frame]
                eventsperAtom.append(event)
                event = numpy.array(
                    [eventsperAtom[-1][CURSTATE], atomTraj[frame], atomTraj[frame], 0],
                    dtype=int,
                )
            event[TIME] += 1
        # append the last event
        eventsperAtom.append(event)
        expectedEvents.append(eventsperAtom)

    events = SOAPify.trackStates(data)
    for atomID in range(data.references.shape[1]):
        for event, expectedEvent in zip(events[atomID], expectedEvents[atomID]):
            assert_array_equal(event, expectedEvent)


def test_residenceTimesFromTracking(input_mockedTrajectoryClassification):
    data = input_mockedTrajectoryClassification
    events = SOAPify.trackStates(data)
    residenceTimesFromTracking = SOAPify.calculateResidenceTimes(data, events)
    expectedResidenceTimes = SOAPify.calculateResidenceTimes(data)

    for stateID in range(len(expectedResidenceTimes)):
        assert_array_equal(
            residenceTimesFromTracking[stateID], expectedResidenceTimes[stateID]
        )
    assert isinstance(events[0], list)


def test_RemoveAtomIdentityFromEventTracker(input_mockedTrajectoryClassification):
    data = input_mockedTrajectoryClassification
    events = SOAPify.trackStates(data)
    newevents = SOAPify.RemoveAtomIdentityFromEventTracker(events)
    # verify that nothing is changed:
    assert isinstance(events[0], list)
    assert isinstance(events, list)
    assert isinstance(events[0][0], numpy.ndarray)
    # verify that the copy is correct:
    assert isinstance(newevents, list)
    count = 0
    for atomID in range(data.references.shape[1]):
        for event in events[atomID]:
            assert_array_equal(event, newevents[count])
            assert isinstance(newevents[atomID], numpy.ndarray)
            count += 1
    # if we pass to the function a list of tracker
    otherevents = SOAPify.RemoveAtomIdentityFromEventTracker(newevents)
    # nothing should happen
    assert otherevents == newevents