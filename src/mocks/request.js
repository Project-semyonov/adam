const tempData = {
    1: {temp: 'Temperature: 80.50, Date: 11-17-2018, Time: 18.11'},
    2: {temp: 'Temperature: 72.30, Date: 01-05-1996, Time: 13.13'},
};

/*export function getTempData(tempDataID){
    return request(tempData).then(tempData => tempData.tempDataID);
}*/

export default function request(tempDataID){
    return new Promise((resolve, reject) => {
        //const tempDataID = getTempData(1)
        process.nextTick(() =>
            tempData[tempDataID]
                ? resolve(tempData[tempDataID])
                : reject({
                    error: 'Temp' + tempDataID + 'not found.',
                }),
        );
    });
}
/*export const tempData = jest.fn();
const mock = jest.fn().mockImplementation(() => {
    return {1: 'Temperature'}
});

export default mock;*/