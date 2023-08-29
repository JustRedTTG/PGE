import pygameextra.event as event
import pygameextra.display as display
import pygame

fingers = []


def handle_finger_events(mouse_as_finger: bool = False):
    if event.c.type == pygame.FINGERDOWN:
        fingers.append({
            'id': event.c.finger_id,
            'pos': (event.c.x * display.get_width(), event.c.y * display.get_height())
        })
    elif event.c.type == pygame.FINGERMOTION:
        i = 0
        while i < len(fingers):
            if fingers[i]['id'] == event.c.finger_id:
                fingers[i]['pos'] = (event.c.x * display.get_width(), event.c.y * display.get_height())
                break
            i += 1
    elif event.c.type == pygame.FINGERUP:
        i = 0
        while i < len(fingers):
            if fingers[i]['id'] == event.c.finger_id:
                del fingers[i]
                i -= 1
            i += 1
    if not mouse_as_finger: return
    if not pygame.mouse.get_pressed()[0]:
        i = 0
        while i < len(fingers):
            if fingers[i]['id'] == 'mouse':
                del fingers[i]
                break
            i += 1
    else:
        i = 0
        while i < len(fingers):
            if fingers[i]['id'] == 'mouse':
                fingers[i]['pos'] = pygame.mouse.get_pos()
                return
            i += 1
        fingers.append({'id': 'mouse', 'pos': pygame.mouse.get_pos()})
