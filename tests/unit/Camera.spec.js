//Camera Testing 

import Camera from '@/components/Camera.vue'
import { mount } from '@vue/test-utils'

describe('Click event', () => {
    it ('Click on update button calls our method getTemp', () => {
      // const wrapper = mount(Camera, {
      //     stubs: {
      //         videoList: '<div @click="chooseVideo(video)" />'
      //     }
      // })
       //wrapper.find('button').trigger('click')
       //expect(wrapper.findAll('.videoList'))
           const wrapper = mount(Camera)
           wrapper.find('button').trigger('click')
        })
    }) 

test('testing ChooseVideo method', () => {
    return Camera.chooseVideo().then((data) => {
        expect(data).toBe('Test.mp4');
    });
})