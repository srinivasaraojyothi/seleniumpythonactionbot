function simulateDragDrop(sourceNode, destinationNode) {
    const DRAG_OVER = 'dragover';
    const DRAG_END = 'dragend';
    const DRAG_START = 'dragstart';
    const DROP = 'drop';

    const createCustomEvent = (type) => {
        const event = new CustomEvent('CustomEvent');
        event.initCustomEvent(type, true, true, null);
        event.dataTransfer = {
            data: {},
            setData (type, val) {
                this.data[type] = val;
            },
            getData (type) {
                return this.data[type];
            },
            // This ensures the directives 'dnd-moved=""' callback is fired
            // on the 'dragend' event, removing the original dragged element..
            dropEffect: 'move'

        };
        return event;
    };

    const dispatchEvent = (node, event) => {
        if (node.dispatchEvent) {
            return node.dispatchEvent(event);
        }
    };

    // dnd-lists >= 2.0.0 uses a custom MIME type of 'application/x-dnd' which it uses to lookup the 'dataTransfer.data' object.
    // If a custom type is added using the 'dnd-type="'xxxx'"' attribute it is appended to the default type i.e 'application/x-dnd-xxxx'.
    // We need to add the type here so dnd-list can access the 'dataTransfer.data' object in the drop event handler.
    const addType = (sourceNode) => {
        const defaultType = 'application/x-dnd';
        const customType = sourceNode.getAttribute('dnd-type');

        if (customType) {
            // Remove single quotes if any present.
            // dnd-list converts any types provided by 'dnd-type="'xXxX'"' to lowercase, so match that here.
            const formattedStr = customType.replace(/'/g,'');
            return [`${defaultType}-${formattedStr.toLowerCase()}`];
        }

        return [defaultType];
    };

    const event = createCustomEvent(DRAG_START);
    event.dataTransfer.types = addType(sourceNode, destinationNode);
    dispatchEvent(sourceNode, event);

    const dragOverEvent = createCustomEvent(DRAG_OVER);
    dragOverEvent.dataTransfer = event.dataTransfer;
    dispatchEvent(destinationNode, dragOverEvent);

    // When the the first element is dragged over the second element a placeholder
    // element will appear, this becomes the element the dragged element drops upon.
    const dropNode = document.querySelector('.dndPlaceholder');

    const dropEvent = createCustomEvent(DROP);
    dropEvent.dataTransfer = event.dataTransfer;
    dispatchEvent(dropNode, dropEvent);

    const dragEndEvent = createCustomEvent(DRAG_END);
    dragEndEvent.dataTransfer = event.dataTransfer;
    dispatchEvent(sourceNode, dragEndEvent);

}
simulateDragDrop(arguments[0], arguments[1]);