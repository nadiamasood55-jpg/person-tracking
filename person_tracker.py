import cv2

# ===============================
# INITIALIZATION
# ===============================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not accessible")
    exit()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

tracker = None
tracking = False

print("Press 's' to START tracking")
print("Press 'x' to STOP tracking")
print("Press 'q' to QUIT")

# ===============================
# MAIN LOOP
# ===============================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ===============================
    # PERSON DETECTION
    # ===============================
    if not tracking:
        boxes, weights = hog.detectMultiScale(
            frame,
            winStride=(8, 8),
            padding=(8, 8),
            scale=1.05
        )

        # Filter weak detections
        filtered_boxes = []
        for i, (x, y, w, h) in enumerate(boxes):
            if weights[i] > 0.4:
                filtered_boxes.append((x, y, w, h))

        # Draw detections
        for (x, y, w, h) in filtered_boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Person", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # ===============================
    # TRACKING
    # ===============================
    if tracking and tracker is not None:
        success, bbox = tracker.update(frame)

        if success:
            x, y, w, h = [int(v) for v in bbox]

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Tracking", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

            # Coordinates
            cv2.putText(frame, f"X:{x} Y:{y}", (x, y + h + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        else:
            cv2.putText(frame, "Tracking Lost!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            tracking = False
            tracker = None

    # ===============================
    # DISPLAY
    # ===============================
    cv2.imshow("Person Tracking System", frame)

    key = cv2.waitKey(1) & 0xFF

    # ===============================
    # START TRACKING
    # ===============================
    if key == ord('s') and not tracking:
        boxes, weights = hog.detectMultiScale(frame)

        if len(boxes) > 0:
            # Pick largest detected person
            (x, y, w, h) = max(boxes, key=lambda b: b[2] * b[3])

            tracker = cv2.TrackerCSRT_create()
            tracker.init(frame, (x, y, w, h))

            tracking = True
            print("Tracking Started")
        else:
            print("No person detected")

    # ===============================
    # STOP TRACKING
    # ===============================
    if key == ord('x'):
        tracking = False
        tracker = None
        print("Tracking Stopped")

    # ===============================
    # EXIT
    # ===============================
    if key == ord('q'):
        break

# ===============================
# CLEANUP
# ===============================
cap.release()
cv2.destroyAllWindows()