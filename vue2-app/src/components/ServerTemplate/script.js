import vtkURLExtract from '@kitware/vtk.js/Common/Core/URLExtract';

export default {
  name: 'TrameServerTemplate',
  inject: ['trame'],
  props: {
    templateName: {
      type: String,
      default: 'main',
    },
    urlKey: {
      type: String,
      default: 'ui',
    },
    useUrl: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      trameTemplateTS: 0,
    };
  },
  computed: {
    tName() {
      if (this.useUrl && vtkURLExtract.extractURLParameters()[this.urlKey]) {
        return vtkURLExtract.extractURLParameters()[this.urlKey];
      }
      return this.templateName;
    },
  },
  created() {
    this.onNewTemplate = () => {
      this.$options.components.trameTemplateInternal = this.trame.state.trameTemplate;
      this.trameTemplateTS = this.trame.state.trameTemplateTS;
    };
    this.trame.$on('trameTemplateChange', this.onNewTemplate);
    this.onNewTemplate();
  },
  beforeDestroy() {
    this.trame.$off('trameTemplateChange', this.onNewTemplate);
  },
};
