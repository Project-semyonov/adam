// TempSensor Testing
import axios from 'axios'
// jest.mock('axios');
// jest.mock('@/mocks/request');
// import request from '@/mocks/request'
import TempSensor from '@/components/TempSensor.vue'
import tempData from '@/components/TempSensor.vue'
// import data from '@/components/TempSensor.vue'
import getTemps from '@/components/TempSensor.vue'
import { mount } from '@vue/test-utils'
jest.mock('axios')

describe('Click event', () => {
  it('Click on update button calls our method getTemp', () => {
    const wrapper = mount(TempSensor)
    wrapper.find('button').trigger('click')
  })
})

test('test axios fetch', () => {
  const res = { data: [{ Temperature: '80.50, Date: 11-17-2018, Time: 18.11' }] }
  axios.get.mockResolvedValue(res)
  return getTemps().then(tempData => expect(tempData).toEqual(res.data))
})

/* test('the fetch fails with an error', () => {
    except.assertions(1);
    return except(TempSensor.getTemp()).reject.toMatch('error');
}); */
/* test('Testing the JSON data from S3 bucket', () => {
    //expect.assertions(1);
    return TempSensor.then(data =>{
        expect(data.temp).toEqual(data);
    });
}); */

/* it('work with promises', () => {
    //except.assertions(1);
    return new promises(TempSensor).then(data => except(data).toEqual(data));
}); */

// working mock of request
/* test('works with promises', () => {
    return expect(request(1)).resolves.toEqual({temp: 'Temperature: 80.50, Date: 11-17-2018, Time: 18.11'});
}); */

/* test('promise', done => {
    function callback(TempSensor) {
        except(TempSensor).toBe('Temperature');
        done();
    }
    request(callback);
}); */

/* test('promise data', async () => {
    const data = await request();
    expect(data).toEqual({1: 'Temperature'});
  }); */

/* jest.mock('axios', () => {
    return {
        get: () => ({data: {video: test.mp4 }})
    }
}) */

/* test('the data is temperature', async () => {
    let data = await TempSensor.data(tempData);
    expect(data).toEqual(expect.anything());
})

test('the data is temperature', async () => {
    let data = await getTemps(tempData);
    expect(data).toEqual(expect.anything());
}) */

it('should throw Error with message "Failed to get temps from the sensor 🚨" when no params were passed', () => {
  try {
    throwError()
    // Fail test if above expression doesn't throw anything.
    expect(true).toBe(false)
  } catch (e) {
    expect(e.message).toEqual('Failed to get temps from the sensor 🚨')
  }
})

test('testing error message', () => {
  expect()
})

test('testing error message', () => {
  expect(() => {
    getTemps('temp')
  }).toThrow()
})

/* console.error = jest.fn();

  beforeEach(() => {
    console.error.mockClear();
  });

  it('testing error message', () => {
    const wrapper = mount(<App />);
    console.log('mockedError', console.error.mock.calls);
    expect(console.error).toHaveBeenCalledTimes(1);
  }); */
